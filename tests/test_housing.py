"""Independent reference dynamics, conservation and nesting for Iacoviello–Neri.

The Dynare fixture uses household-level equations, rather than this library's
reduced resource equation. Both apply the explicit source reconciliations in the
model specification. No estimation results are claimed by these checks.
"""
import json
from pathlib import Path

import numpy as np
import pytest
import yaml

from modellib import Composition
from modellib.compose import load_component
from modellib.lre import irf

ROOT = Path(__file__).resolve().parent.parent
ENTRY = ROOT / "models" / "iacoviello-neri-2010"
MANIFEST = yaml.safe_load((ENTRY / "manifest.yaml").read_text())
CORE = MANIFEST["composition"]["core"]
BLOCKS = MANIFEST["composition"]["blocks"]
REFERENCE = json.loads((ROOT / "tests" / "fixtures" /
                        "iacoviello_neri_2010_reference.json").read_text())
SHOCK_MAP = {
    "eps_c": "eps_c_in", "eps_h": "eps_h_in", "eps_k": "eps_k_in",
    "eps_j": "eps_j_in", "eps_t": "eps_tau_in", "eps_z": "eps_z_in",
    "eps_p": "eps_p_in", "eps_e": "eps_R_in", "eps_s": "eps_s_in",
}


@pytest.fixture(scope="module")
def full():
    c = Composition(CORE, BLOCKS)
    return c, *c.solve()


def test_reference_is_a_determinate_matching_first_order_profile(full):
    c, P, Q, _ = full
    assert len(c.variables) == len(c.equations) == 46
    assert P.shape == (46, 46) and Q.shape == (46, 9)
    assert set(c.shocks) == set(SHOCK_MAP.values())
    assert max(abs(np.linalg.eigvals(P))) < 1
    d = REFERENCE["diagnostics"]
    assert d["blanchard_kahn_satisfied"] and d["blanchard_kahn_info"] == 0
    assert d["unstable_roots"] == d["forward_looking_variables"] == 18
    assert d["static_residual_max"] < 1e-12
    assert REFERENCE["engine"]["order"] == 1
    assert REFERENCE["profile"] == "paper_consistent_article_means"


@pytest.mark.parametrize("source_shock", SHOCK_MAP)
def test_all_direct_variables_match_independent_dynare_paths(full, source_shock):
    c, P, Q, _ = full
    path = irf(P, Q, c.shock_index(SHOCK_MAP[source_shock]), 20)
    for source_name, name in REFERENCE["variable_names_canonical"].items():
        expected = REFERENCE["irfs_unit_canonical_shock"][source_shock][source_name]
        np.testing.assert_allclose(path[:, c.index(name)], expected, atol=1e-7,
                                   rtol=1e-7, err_msg=f"{source_shock}: {name}")


def test_balanced_growth_and_primitive_steady_state(full):
    _, _, _, p = full
    # Independently recover levels from production, fixed land one, and the
    # reported output ratios. Compare to the nonlinear Dynare steady state.
    gy, gk, gh = (p[f"in_growth_{s}"] for s in ("y", "k", "h"))
    assert gk / gy == pytest.approx(np.exp(p["gamma_ak_in"]))
    assert p["in_growth_q"] * gh == pytest.approx(gy)
    nc = p["in_nc_p"]**p["alpha_patient"] * p["in_nc_i"]**(1-p["alpha_patient"])
    Y = (p["in_kcy"] / gk)**(p["mu_c"] / (1-p["mu_c"])) * nc
    kc, kh = p["in_kcy"]*Y, p["in_khy"]*Y
    nh = p["in_nh_p"]**p["alpha_patient"] * p["in_nh_i"]**(1-p["alpha_patient"])
    materials = p["mu_b"] * p["in_qiy"] * Y
    IH = ((kh/gy)**p["mu_h"] * materials**p["mu_b"] *
          nh**(1-p["mu_h"]-p["mu_b"]-p["mu_land"]))
    q = p["in_qiy"] * Y / IH
    cp, ci = p["in_cpy"]*Y, p["in_ciy"]*Y
    hp, hi = p["in_qhpy"]*Y/q, p["in_qhiy"]*Y/q
    debt = p["in_by"]*Y
    lm = (1-p["beta_impatient"]/p["beta_patient"]) / ci
    levels = dict(Y=Y, kc=kc, kh=kh, I=IH, q=q, c=cp, c1=ci, h=hp,
                  h1=hi, b=debt, lm=lm)
    assert min(levels.values()) > 0
    for name, value in levels.items():
        assert np.log(value) == pytest.approx(
            REFERENCE["diagnostics"]["steady_state"][name], abs=1e-11)
    # Resource accounting, borrower budget, housing stock and collateral.
    investment = kc-(1-p["delta_k_c"])*kc/gk + kh-(1-p["delta_k_h"])*kh/gy
    assert Y == pytest.approx(cp+ci+investment+materials, abs=1e-12)
    income = Y*(p["in_wcin_y"]+p["in_whiny"])
    assert ci+q*hi*(1-(1-p["delta_housing"])/gh) == pytest.approx(
        income+debt-p["in_r_ss"]*debt/gy, abs=1e-12)
    assert IH == pytest.approx((hp+hi)*(1-(1-p["delta_housing"])/gh))
    assert p["in_r_ss"]*debt == pytest.approx(p["ltv_in"]*p["in_growth_q"]*q*hi)
    # Compare rounded Table 2 ratios at the article's printed precision.
    assert round(100*(cp+ci)/(Y*p["in_gdpy"])) == 67
    assert round(100*investment/(Y*p["in_gdpy"])) == 27
    assert round(100*q*IH/(Y*p["in_gdpy"])) == 6
    assert q*(hp+hi)/(4*Y*p["in_gdpy"]) == pytest.approx(1.36, abs=.01)


@pytest.mark.parametrize("shock", SHOCK_MAP.values())
def test_collateral_stocks_and_aggregate_accounting_at_every_horizon(full, shock):
    c, P, Q, p = full
    path = irf(P, Q, c.shock_index(shock), 25)
    z = np.zeros(24)
    v = lambda name: path[:24, c.index(name)]
    lead = lambda name: path[1:25, c.index(name)]
    lag = lambda name: np.r_[0., path[:23, c.index(name)]]
    np.testing.assert_allclose(v("b_borrower"), lead("q_h")+v("h_impatient")-
                               v("i")+lead("pi"), atol=1e-8)
    housing = p["in_qhpy"]*v("h_patient")+p["in_qhiy"]*v("h_impatient")
    old_housing = p["in_qhpy"]*lag("h_patient")+p["in_qhiy"]*lag("h_impatient")
    np.testing.assert_allclose(housing-(1-p["delta_housing"])/p["in_growth_h"]*
                               old_housing-p["in_qiy"]*v("inv_h"), z, atol=1e-8)
    # Costs have nonzero first derivatives despite zero steady-state levels.
    usage = (p["in_rkc_ss"]*p["in_kcy"]/p["in_growth_k"]*v("u_c")+
             p["in_rkh_ss"]*p["in_khy"]/p["in_growth_y"]*v("u_h"))
    resource = (v("y_c")-p["in_cy"]*v("c")-p["in_iky"]*v("inv")+
                p["in_ikcy"]*v("a_k_in")-
                p["mu_b"]*p["in_qiy"]*(v("q_h")+v("inv_h"))-usage)
    np.testing.assert_allclose(resource, z, atol=1e-8)
    np.testing.assert_allclose(p["in_gdpy"]*v("y"),
        p["in_cy"]*v("c")+p["in_iky"]*v("inv")+p["in_qiy"]*v("inv_h"), atol=1e-8)
    hours = sum(p[coef]*v(name) for coef,name in [
        ("in_nc_p","n_c_patient"),("in_nc_i","n_c_impatient"),
        ("in_nh_p","n_h_patient"),("in_nh_i","n_h_impatient")])
    np.testing.assert_allclose(p["in_total_n"]*v("n"), hours, atol=1e-8)
    payroll = sum(p[coef]*(v(w)+v(n)) for coef,w,n in [
        ("in_wcpny","w_c_patient","n_c_patient"),
        ("in_wcin_y","w_c_impatient","n_c_impatient"),
        ("in_whpny","w_h_patient","n_h_patient"),
        ("in_whiny","w_h_impatient","n_h_impatient")])
    np.testing.assert_allclose(p["in_total_wn_y"]*(v("w")+v("n")), payroll, atol=1e-8)


@pytest.mark.parametrize("block,overrides", [
    ("internal-habit-consumption-in", {"habit_patient":0, "habit_impatient":0}),
    ("capital-stock-adjustment-in", {"phi_k_c":0, "phi_k_h":0}),
    ("sectoral-capital-utilisation-in", {"zeta_in":1}),
    ("calvo-prices-indexation-in", {"theta_p_in":0}),
    ("sectoral-calvo-wages-in", {"theta_w_c_in":0, "theta_w_h_in":0}),
])
def test_friction_limit_recovers_composition_without_the_block(block, overrides):
    with_block = Composition(CORE, BLOCKS)
    without = Composition(CORE, [b for b in BLOCKS if b != block])
    P, Q, _ = with_block.solve(overrides)
    P0, Q0, _ = without.solve()
    for shock in set(with_block.shocks) & set(without.shocks):
        a = irf(P, Q, with_block.shock_index(shock), 12)
        b = irf(P0, Q0, without.shock_index(shock), 12)
        for name in without.variables:
            np.testing.assert_allclose(a[:,with_block.index(name)],
                                       b[:,without.index(name)], rtol=1e-7, atol=1e-7)


@pytest.mark.parametrize("shock,restrictions", [
    ("eps_j_in", {"q_h":1, "inv_h":1}),
    ("eps_h_in", {"q_h":-1, "inv_h":1}),
    ("eps_R_in", {"i":1, "q_h":-1, "inv_h":-1, "c":-1, "y":-1}),
])
def test_economic_orientation_of_key_innovations(full, shock, restrictions):
    c, _, Q, _ = full
    for variable, sign in restrictions.items():
        assert sign*Q[c.index(variable),c.shock_index(shock)] > 0


def test_profile_means_priors_and_shock_units_match_published_tables(full):
    _, _, _, params = full
    est = yaml.safe_load((ENTRY / "estimation.yaml").read_text())
    assert est["status"] == "published-reference-only"
    assert est["observations"]["estimation_sample"]["quarters"] == 168
    assert len(est["observations"]["measurement_system"]) == 10
    assert len(est["observations"]["measurement_errors"]) == 2
    assert len(est["structural_table_3"]) == 22
    assert len(est["shock_table_4"]) == 17
    components = [load_component(cid) for cid in [CORE]+BLOCKS]
    declared = {p["name"]:p for component in components for p in component["parameters"]}
    shocks = {s["id"]:s for component in components for s in component["shocks"]}
    for row in est["structural_table_3"]+est["shock_table_4"]:
        assert row["p025"] <= row["median"] <= row["p975"]
        assert row["p025"] <= row["mean"] <= row["p975"]
        assert "mode" not in row  # The paper reports medians, not modes.
        scale = .01 if row.get("name", "").startswith("gamma_") else 1.
        if "name" in row:
            item = declared[row["name"]]
            assert params[row["name"]] == pytest.approx(scale*row["mean"])
            assert item["prior"]["family"] == row["prior"][0]
            assert item["prior"]["hyperparameters"] == pytest.approx(
                [scale*v for v in row["prior"][1:]])
        elif row["shock"] in shocks:
            assert shocks[row["shock"]]["sd"] == pytest.approx(row["mean"])
    for row in est["fixed_calibrations"]["values"]:
        assert params[row["component_parameter"]] == pytest.approx(row["value"])
    assert est["estimation_procedure"]["mh"]["reported_draws"] == 500000
    profiles = yaml.safe_load((ENTRY / "parameter-profiles.yaml").read_text())
    assert params["phi_pi_in"] == 1.44
    assert profiles["profiles"]["numerical-reference"]["overrides"]["phi_pi_in"] == 1.40444
