# Independent Iacoviello–Neri numerical reference

`iacoviello_neri_2010_reference.json` contains first-order responses calculated
with Dynare 5.3 and Octave 7.3 from the authors' numerical reference, independently
of `modellib`. The original model, steady-state routine, article and estimation
data are not included. The `provenance.source_mod_sha256` identifies the input
model. Article: Iacoviello and Neri (2010), *AEJ: Macroeconomics* 2(2), 125–164,
[doi:10.1257/mac.2.2.125](https://doi.org/10.1257/mac.2.2.125).

The reference is a **budget-consistent article-mean profile**, rather than the
unmodified numerical programme or a posterior-estimation result. The economic
choices are documented in the [model specification](../../models/iacoviello-neri-2010/spec/model.md).
They are essential when reproducing these quantities:

1. Use Table 1 fixed parameters and Tables 3–4 posterior means at printed
   precision. `provenance.parameter_overrides` records reference parameter names
   and values, including the negative sign mapping between `NU` and `xi_patient`.
2. Derive internal-habit marginal utility directly from utilities (1)–(2).
   The continuation term carries the next-period preference weight, not the
   current weight.
3. Restore sectoral utilisation expenditures in the patient budget B1 and net
   capital returns B4–B5, using Appendix B's cost functions. Their level is zero
   but their first derivative is nonzero at unit utilisation. Capital adjustment
   cost levels and first derivatives vanish on the balanced-growth path; retain
   their derivatives in the capital Euler conditions.
4. Retain the sector-specific housing-wage slope, exponential trend convention,
   and expenditure GDP weights from the numerical reference. This does not
   simultaneously assert the inconsistent printed B34 resource identity or
   B33 production-side GDP expression.
5. Solve the deterministic steady state, request all endogenous variables with
   `stoch_simul(order=1,irf=20,nograph,noprint)`, and export `oo_.irfs`, `M_.Sigma_e`,
   the static residuals and the `check` determinacy result.
6. Divide each response by its shock SD to obtain a unit innovation. For `eps_s`,
   multiply the resulting responses by 100 because one canonical innovation
   equals 100 native innovation units; divide the `a_s` output itself by 100.
   No other fitted scaling or sign adjustment is applied.

Arrays are indexed by reference shock name, reference variable name, and horizon
(index zero is impact). `shock_names_canonical` and `variable_names_canonical`
provide the crosswalk. All compared responses are log deviations per unit
canonical innovation; rates remain quarterly. The steady-state section contains
logs of positive stationary levels, not the zero deviations returned by the
linear library representation. Structural shock SDs and engine information are
retained so units and approximation order can be checked independently.

The enduring comparisons are in `tests/test_housing.py`; the golden targets
select economically meaningful responses from this fixture. Tolerances are
absolute and relative `1e-7` in unit-shock log units. Matching these numbers tests
the documented fixed-parameter equation system. It does not reproduce the paper's
posterior uncertainty, historical decompositions or data likelihood.
