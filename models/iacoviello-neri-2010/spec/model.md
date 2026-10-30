# Iacoviello and Neri (2010): housing market spillovers

The canonical reference is Iacoviello and Neri (2010), “Housing Market Spillovers:
Evidence from an Estimated DSGE Model”, *American Economic Journal:
Macroeconomics* 2(2), 125–164,
[doi:10.1257/mac.2.2.125](https://doi.org/10.1257/mac.2.2.125).
The entry represents first-order dynamics around a balanced-growth path with a
locally binding borrowing limit. It is an estimated canonical model; the
[estimation reference](estimation.md) records the paper's Bayesian method,
observables and published posterior distributions separately from the numerical
solution at fixed parameter values.

The equations use a **budget-consistent interpretation** of the published system.
Three source inconsistencies require explicit treatment: the internal-habit
preference shock differs in the numerical reference, the printed patient
housing-wage slope repeats the other sector's stickiness symbol, and B34 omits
utilisation resource costs contained in the patient budget. These issues prevent
a claim that every printed and reference-code equation is reproduced unchanged.

## Households and production

Patient households own productive capital, land and retail firms and lend to
impatient households. Both groups consume, own houses and supply labour to
nonhousing production and construction. Their preferences include internal
consumption habits, a logarithmic housing service flow and a labour aggregate
that allows imperfect substitution between sectors. Each group has measure one;
$\alpha_p$ is the patient **labour-income share**, rather than a population share.

Borrower debt is limited by the expected discounted nominal value of housing.
The strict discount-factor inequality $\beta_b<\beta_p$ yields a positive
steady-state constraint multiplier. The local solution keeps the constraint
binding. This solution does not describe occasional binding, defaults or crisis
regime changes.

Nonhousing production combines household labour composites and utilised
predetermined capital. Construction also uses materials and fixed land.
Consumption-good retail prices are Calvo sticky, while house prices are flexible.
Four labour unions introduce wage stickiness for each household/sector pair.
Sector-specific utilisation and capital-stock adjustment costs govern patient
capital choices. The interest-rate rule responds to inflation and expenditure
GDP growth, with smoothing, a monetary innovation and a persistent inflation
objective disturbance.

The reusable derivations are in [housing and collateral](../../../docs/theory/housing-and-collateral.md),
[two-sector production](../../../docs/theory/two-sector-housing-production.md),
[consumption and capital](../../../docs/theory/consumption-and-capital.md),
[price setting](../../../docs/theory/price-setting.md), and
[wage setting](../../../docs/theory/wage-setting.md).

## Modular composition

| Component | Economic content |
| --- | --- |
| `core-housing-in` | Production, factor demand, labour supply, household and aggregate identities, stationary technology and preference processes |
| `housing-collateral-in` | Binding borrower debt, multiplier and housing collateral services |
| `internal-habit-consumption-in` | Household-specific internal-habit marginal utilities |
| `capital-stock-adjustment-in` | Two sectoral capital Euler equations with stock adjustment costs |
| `sectoral-capital-utilisation-in` | Two utilisation margins and their rental normalisations |
| `calvo-prices-indexation-in` | Indexed nonhousing price Phillips curve and cost-push innovation |
| `sectoral-calvo-wages-in` | Four indexed wage equations with household-specific discounting |
| `taylor-rule-in` | GDP-growth policy rule and inflation-objective process |

The core has habit-free, frictionless investment, fixed-utilisation and flexible
nominal closures that the corresponding mechanisms replace. The policy variable
is GDP growth; a parallel flexible-price output gap is unnecessary. Existing
external-habit and investment-flow-adjustment mechanisms have different
primitives and are therefore not substitutes for these components.

## Symbols, units and timing

All retained endogenous variables are first-order log deviations from stationary
steady-state levels. Inflation `pi` and the nominal rate `i` are quarterly log-rate
deviations. Exogenous state variables are log deviations; innovations have the
natural-log units of the published shock standard deviations. Multiplication by
100 expresses quantity responses in percent and rate responses in quarterly
percentage points. Patient lending and borrower debt are the same positive
steady-state asset, represented by `b_borrower`; negative deviations do not mean
negative debt levels.

| Paper | Numerical-reference notation | Repository variable or parameter |
| --- | --- | --- |
| $c,c'$ | `c,c1` | `c_patient,c_impatient` |
| $h,h'$ | `h,h1` | `h_patient,h_impatient` |
| $u_c,u'_c$ | `uc,uc1` | `uc_patient,uc_impatient` |
| $n_c,n'_c,n_h,n'_h$ | `nc,nc1,nh,nh1` | `n_c_patient,n_c_impatient,n_h_patient,n_h_impatient` |
| $w_c,w'_c,w_h,w'_h$ | `wc,wc1,wh,wh1` | `w_c_patient,w_c_impatient,w_h_patient,w_h_impatient` |
| $X_{wc},X'_{wc},X_{wh},X'_{wh}$ | `xwc,xwc1,xwh,xwh1` | `xw_c_patient,xw_c_impatient,xw_h_patient,xw_h_impatient` |
| $k_c,k_h$ | `kc,kh` | `k_c,k_h` |
| $R_c,R_h$ | `rkc,rkh` | `rk_c,rk_h` |
| $z_c,z_h$ | `zkc,zkh` | `u_c,u_h` |
| $Y,IH,q,X$ | `Y,I,q,X` | `y_c,inv_h,q_h,x_price` |
| $b',\lambda$ | `b,lm` | `b_borrower,lambda_borrower` |
| $C,IK,GDP$ | aggregate observation auxiliaries | `c,inv,y` |
| $\pi,R$ | `dp,r` | `pi,i` |
| $Z_c,Z_h,Z_k,j,\tau,z,s$ | `a_c,a_h,a_k,a_j,a_t,a_z,a_s` | `a_c_in,a_h_in,a_k_in,a_j_in,a_tau_in,a_z_in,a_s_in` |
| $\alpha$ | `ALPHA` | `alpha_patient` |
| $\epsilon,\epsilon'$ | `EC,EC1` | `habit_patient,habit_impatient` |
| $\xi,\xi'$ | `-NU,-NU1` | `xi_patient,xi_impatient` |
| $\phi_{kc},\phi_{kh}$ | `FIKC,FIKH` | `phi_k_c,phi_k_h` |

The remaining structural parameter and innovation names are:

| Paper | Numerical reference | Repository |
| --- | --- | --- |
| $\beta,\beta'$ | `BETA,BETA1` | `beta_patient,beta_impatient` |
| $j,m$ | `JEI,M` | `j_housing,ltv_in` |
| $\mu_c,\mu_h,\mu_b,\mu_l$ | `MUC,MUH,MUBB,KAPPA` | `mu_c,mu_h,mu_b,mu_land` |
| $\delta_{kc},\delta_{kh},\delta_h$ | `DKC,DKH,DH` | `delta_k_c,delta_k_h,delta_housing` |
| $\bar X,\bar X_{wc},\bar X_{wh}$ | `X_SS,XW_SS,XW_SS` | `markup_p_in,markup_w_in,markup_w_in` |
| $\eta,\eta'$ | `ETA,ETA1` | `eta_patient,eta_impatient` |
| $\theta_\pi,\iota_\pi$ | `TETA,LAGP` | `theta_p_in,iota_p_in` |
| $\theta_{wc},\theta_{wh}$ | `TETAWC,TETAWH` | `theta_w_c_in,theta_w_h_in` |
| $\iota_{wc},\iota_{wh}$ | `LAGWC,LAGWH` | `iota_w_c_in,iota_w_h_in` |
| $\zeta$ | `ZETAKC` | `zeta_in` |
| $r_R,r_\pi,r_Y$ | `TAYLOR_R,TAYLOR_P,TAYLOR_Y` | `rho_i_in,phi_pi_in,phi_growth_in` |
| $\gamma_{AC},\gamma_{AH},\gamma_{AK}$ | `TREND_AC,TREND_AH,TREND_AK` | `gamma_ac_in,gamma_ah_in,gamma_ak_in` |
| $\rho_{AC},\rho_{AH},\rho_{AK}$ | `RHO_AC,RHO_AH,RHO_AK` | `rho_c_in,rho_h_in,rho_k_in` |
| $\rho_j,\rho_\tau,\rho_z,\rho_s$ | `RHO_AJ,RHO_AT,RHO_AZ,RHO_AS` | `rho_j_in,rho_tau_in,rho_z_in,rho_s_in` |
| $u_C,u_H,u_K$ | `eps_c,eps_h,eps_k` | `eps_c_in,eps_h_in,eps_k_in` |
| $u_j,u_\tau,u_z$ | `eps_j,eps_t,eps_z` | `eps_j_in,eps_tau_in,eps_z_in` |
| $u_R,u_p,u_s$ | `eps_e,eps_p,eps_s` | `eps_R_in,eps_p_in,eps_s_in` |
| $IK_c,IK_h$ | Differences of `kc,kh` | `inv_k_c,inv_k_h` |
| Aggregate hours and wages | Constructed aggregates | `n,w` |

The repository aggregate `n` is the sum of all four household/sector hours in
levels, linearised with steady-hours weights. Aggregate `w` is gross total
labour income divided by those total hours; its linearisation includes the
changes in household/sector employment as well as wage changes. The ten-observable reference additionally defines sectoral
nominal wage inflation by differentiating the sum of household wage levels.
Those observation auxiliaries are distinct from `w`, and their equations and
weights are recorded in `estimation.md` and `estimation.yaml`. Eliminated $k_b,l,
p_b,R_l,p_l$ and the patient bond position have no separate retained variable.

Capital dated $t-1$ produces at $t$. Nominal debt dated $t-1$ repays at
$R_{t-1}/\Pi_t$. The borrowing limit values houses at expected $q_{t+1}\Pi_{t+1}/R_t$.
These distinct interest-rate timings are retained. The code's `NU=-xi`
normalisation changes parameter signs, not the economics of labour mobility.

## Source equation crosswalk

Physical PDF page numbers below are one-based: printed page minus 124.
The table covers the complete Appendix B equilibrium. Growth and utility
relations outside its numbered system are listed afterwards.

| Source | Printed page (PDF page) | Content and treatment |
| --- | --- | --- |
| B1 | 159 (35) | Full patient budget, including dividends, land and utilisation costs; implied by goods clearing and borrower budget in the reduced system |
| B2 | 160 (36) | Patient housing Euler equation |
| B3 | 160 (36) | Patient bond Euler equation |
| B4 | 160 (36) | Nonhousing capital optimum; net utilisation return and stock adjustment |
| B5 | 160 (36) | Construction capital optimum; net utilisation return and stock adjustment |
| B6 | 160 (36) | Patient nonhousing labour supply and wage markup |
| B7 | 160 (36) | Patient construction labour supply and wage markup |
| B8 | 160 (36) | Material price equals one; substituted into material demand |
| B9 | 160 (36) | Nonhousing utilisation choice, including investment technology |
| B10 | 160 (36) | Construction utilisation choice |
| B11 | 160 (36) | Land valuation; recovered from rents and patient discounting after fixed land is imposed |
| B12 | 160 (36) | Borrower budget, with union dividends restoring gross labour income |
| B13 | 160 (36) | Binding expected-value borrowing limit |
| B14 | 160 (36) | Borrower housing Euler equation, including collateral service |
| B15 | 160 (36) | Borrower bond optimum and positive constraint multiplier |
| B16 | 161 (37) | Borrower nonhousing labour supply and wage markup |
| B17 | 161 (37) | Borrower construction labour supply and wage markup |
| B18 | 161 (37) | Nonhousing Cobb–Douglas production |
| B19 | 161 (37) | Construction production, with materials substituted and land fixed |
| B20 | 161 (37) | Patient nonhousing labour demand |
| B21 | 161 (37) | Borrower nonhousing labour demand |
| B22 | 161 (37) | Patient construction labour demand |
| B23 | 161 (37) | Borrower construction labour demand |
| B24 | 161 (37) | Nonhousing capital-services demand |
| B25 | 161 (37) | Construction capital-services demand |
| B26 | 161 (37) | Land rent share; substituted in patient income and land valuation |
| B27 | 161 (37) | Material share; substituted using $p_b=1$ |
| B28 | 161 (37) | Indexed price Phillips curve with IID cost-push innovation |
| B29 | 161 (37) | Patient nonhousing wage Phillips curve |
| B30 | 161 (37) | Borrower nonhousing wage Phillips curve |
| B31 | 161 (37) | Patient construction wage Phillips curve; use construction-sector stickiness in its derived slope |
| B32 | 161 (37) | Borrower construction wage Phillips curve |
| B33 | 162 (38) | Smoothed monetary rule; expenditure GDP follows main-text footnote 15 |
| B34 | 162 (38) | Goods clearing; adapted to include utilisation costs implied by B1 |
| B35 | 162 (38) | Housing stock-flow identity |
| B36 | 162 (38) | Unit aggregate land; imposed before reduction |

Main-text equations (1)–(2), printed pp. 128–129 (PDF pp. 4–5), define preferences
and internal-habit derivatives. Equations (3)–(5), pp. 129–130 (PDF pp. 5–6),
are the household budgets and borrowing limit; (6)–(7), p. 131 (PDF p. 7),
are production; (8)–(9), p. 132 (PDF p. 8), are pricing and policy;
(10)–(11), p. 133 (PDF p. 9), are market clearing. Equations (12)–(15),
pp. 133–134 (PDF pp. 9–10), define balanced growth. The dividend, adjustment-cost
and utilisation functions follow B36 on p. 162 (PDF p. 38). Shock laws appear in
Sections I.A, I.C and I.E. Observation relations are documented in the separate
[estimation specification](estimation.md).

## Accounting interpretation and source boundaries

The full theoretical system has land, land rent and price, materials and both bond
positions. Fixed land, the material-price optimum, factor shares and loan clearing
eliminate those auxiliary quantities. Their economic restrictions remain in
construction technology, patient income and the household wealth interpretation.
In particular, fixed land has a scarcity value; it is not a zero-value input.

B1 contains utilisation costs while B34 omits them. With positive marginal
utilisation cost at unit utilisation, those terms survive first-order aggregation.
This entry therefore uses goods clearing derived from the household budgets and
net capital returns. The resource equation is explicitly **adapted**; agreement
with the printed B34 alone would not verify full-budget consistency.

Footnote 15, printed p. 132 (PDF p. 8), defines policy GDP as fixed-price
consumption plus business and residential investment. B33 also gives a
production-side expression $Y-k_b+\bar qIH$. Once utilisation costs are retained,
that expression includes their resource use and differs from final expenditure.
The entry selects the expenditure definition for policy and labels this convention
explicitly. Short-run house-price fluctuations do not enter GDP mechanically.

The internal-habit continuation derivative uses tomorrow's preference shock as
required by the utility primitive. The apparent p. 162 housing-wage symbol typo is
resolved by deriving the slope with the housing Calvo probability. The named
`numerical-reference` **parameter** profile preserves its distinct parameter values but
uses the same budget-consistent economics for controlled numerical comparisons.
An unmodified numerical-reference comparison addresses a different equation set.

## Calibration, growth and numerical interpretation

The default structural calibration uses the rounded posterior **means** in Tables
3–4, not the medians, and the fixed values in Table 1. Published percent-scaled
technology trend entries are divided by 100. The separately named `numerical-reference`
profile is a distinct set of point values, not additional decimal precision for
the paper's reported means. Full published statistics remain in
[`../estimation.yaml`](../estimation.yaml).

Growth transformations, steady capital investment ratios and positive asset
levels follow the [balanced-growth derivation](../../../docs/theory/two-sector-housing-production.md#balanced-growth-and-stationary-quantities).
The paper's steady ratios in Table 2 are rounded reference quantities; changes in
trend interpretation, parameter precision and accounting conventions can change
those values. They are not exact restrictions imposed on all parameter profiles.

A first-order solution can verify residuals, accounting identities, determinacy
and matched responses at fixed parameters. Such checks cannot establish the
published posterior distribution, likelihood, historical decomposition or
occasionally binding dynamics. The empirical reference records those results as
published evidence.

## Selecting a parameter profile

[`../parameter-profiles.yaml`](../parameter-profiles.yaml) lists coefficient
overrides for controlled comparisons. The default composition already uses
`paper-posterior-mean`. To select the alternative with the Python API from the
repository root:

```python
from pathlib import Path
import yaml
from modellib.compose import Composition

entry = Path("models/iacoviello-neri-2010")
manifest = yaml.safe_load((entry / "manifest.yaml").read_text())
profiles = yaml.safe_load((entry / "parameter-profiles.yaml").read_text())
composition = Composition(**manifest["composition"])
overrides = profiles["profiles"]["numerical-reference"]["overrides"]
solution = composition.solve(overrides=overrides)
```

The profile selects coefficients in the same economic equation system. It does
not execute the original estimation, change the shock normalisation or restore
the original reference programme's equation discrepancies. Shock SDs and
measurement-error SDs remain separately identified published information;
impulse-response magnitudes require an explicitly chosen innovation size.
