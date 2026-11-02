# Differences between the published paper and numerical reference

The authors' numerical reference represents the same broad two-household, two-sector housing model as Iacoviello and Neri (2010), but differs in several economic equations, parameter values and estimation settings. The repository model is a **budget-derived reconciliation with explicit adaptations**. Neither an unchanged execution of the reference programme nor the entry establishes exact reproduction of all printed equations or the published Bayesian results.

The controlling publication is Iacoviello and Neri (2010), *American Economic
Journal: Macroeconomics* 2(2), 125–164,
[doi:10.1257/mac.2.2.125](https://doi.org/10.1257/mac.2.2.125), including Appendices A/B.
The numerical reference compared here is identified by SHA-256
`e758e9fe45c1ea1839d91067943b747214cab8ee5e3ad0953747ecc72201a90a`.
Code line numbers refer to that version. It is distinct from the authors' original
estimation system, which is not reproduced here. Paper pages are printed pages;
one-based physical PDF page equals printed page minus 124.

The [model specification](model.md), [estimation interpretation](estimation.md)
and [parameter profiles](../parameter-profiles.yaml) state the runnable scope and
reference information. The original article, external numerical source and data
are not redistributed.

## Economic equations

| Issue | Published paper | Numerical reference | Repository model |
| --- | --- | --- | --- |
| Internal habits and preference-shock timing | Utilities (1)–(2), p.128, imply a continuation derivative weighted by the next-period preference shock. | Lines 325–330 factor the current shock outside both current and continuation terms. | Includes the expected future preference weight. This changes the preference-shock transmission at first order. |
| Utilisation expenditures and net returns | B1, p.159, includes utilisation expenditure; B5, p.160, subtracts it from capital returns. B9–B10 and the p.162 cost functions imply positive marginal utilisation cost. | Lines 220–222 omit the expenses from the patient budget; lines 232–241 omit them from net capital returns, while lines 355–356 retain utilisation optimality conditions. | Retains expenses in resources and net returns. Since a(1)=0 but a′(1)>0, these costs affect first-order resources. Their direct utilisation derivative cancels the corresponding gross-rental derivative in net returns. |
| Aggregate goods clearing | Main equation (10), p.133, and B34, p.162, omit utilisation costs even though B1 includes them. | Summing the coded household budgets also omits these costs. | Follows the household-budget derivation, explicitly adapting aggregate clearing relative to (10)/B34. This is an internal inconsistency in the printed system, not simply code disagreement with one unambiguous paper equation. |
| Patient housing-wage slope | The p.162 coefficient ε_wh uses consumption-sector θ_wc, despite being the housing-wage coefficient. | Lines 344–346 use housing-sector `TETAWH`. | Retains housing-sector stickiness, supported by the sector-specific reset problem. The printed formula appears typographically inconsistent. |
| Nonhousing capital resale sign | Printed B4, p.160, literally subtracts [a(z)+1−δ]/A_k. Positive undepreciated capital in B1 and the analogous B5 imply +[1−δ−a(z)]/A_k. | Lines 232–234 use positive undepreciated resale value, while omitting utilisation costs. | Uses positive resale value and negative utilisation cost, derived from B1. Thus it does not transcribe B4 literally. This is an apparent publication typo inferred from the budget, without an author-confirmed erratum. |
| Policy GDP | Footnote 15, p.132, defines fixed-price expenditure GDP as consumption plus business and residential investment. Text following B33, p.162, instead gives goods output less materials plus fixed-price residential investment. | Lines 372–374 use fixed-share expenditure aggregation, following footnote 15. | Retains expenditure GDP. The printed production expression can differ once the retained costs and investment-efficiency conventions are accounted for. It is not asserted to be an identical definition. |

The internal-habit derivative, suppressing household subscripts, is

$$
u_{c,t}=\Gamma\left[\frac{z_t}{c_t-\epsilon c_{t-1}}
-\beta G_C\epsilon E_t\left(\frac{z_{t+1}}{c_{t+1}-\epsilon c_t}\right)\right].
$$

The code places $z_t$ outside the entire bracket. This is a timing discrepancy, rather than a different name or unit for the same shock.

Capital-stock adjustment costs are different from utilisation costs: their level and first derivative vanish along balanced growth, so excluding their level from a first-order budget is legitimate. Their Euler-equation effects are retained. The code's budget omissions should therefore not all be classified as equally consequential.

## Numerical values and estimation

The code's hard-coded parameters labelled as means are a distinct set of point values. Several cannot be obtained merely by rounding the paper's posterior means. Examples, expressed in comparable parameter units:

| Parameter | Paper posterior mean | Numerical reference |
| --- | ---: | ---: |
| Inflation response in policy rule | 1.44 | 1.40444 |
| Patient sectoral labour curvature ξ | 0.66 | 0.68330, stored as NU = −0.68330 |
| Goods-sector capital adjustment curvature | 14.25 | 14.47013 |
| Housing-sector capital adjustment curvature | 10.90 | 11.02808 |
| Goods-technology persistence | 0.95 | 0.94265 |
| Inflation-objective innovation SD | 0.0004 | 0.00034 in natural-log units |

The evidence does not establish why the sets differ. The entry uses the paper's printed means as defaults and preserves the code's structural coefficients as a separate parameter profile. Selecting that profile changes coefficients within the reconciled equations; it does not restore the original programme's equation omissions. Shock standard deviations remain separate metadata, and unit-shock comparisons require no fitted scaling.

For estimation, Table 4, p.139, gives the housing-technology persistence prior SD as **0.10**; the code uses **0.09** at line 480. Footnote 26, pp.139–140, says the published tables and figures are based on **500,000 Metropolis draws**, with approximately **25% acceptance** and convergence assessed by comparing the two halves. The optional code requests **5,000** repetitions, proposal scale 0.2, one block, four presample observations and its own initialisation options (lines 512–522). The printed paper does not specify every corresponding option, so those extra settings cannot all be classified as demonstrated disagreements.

The reference programme defaults to `DO_IRFS=1` and `DO_ESTIMATION=0` (lines 120–121), producing first-order, 20-quarter responses at fixed parameters. Its authors state at lines 24–25 that they used separate estimation code and that this file reproduces only some basic findings. These fixed-parameter responses do not reproduce the paper's posterior-distribution plots, historical decompositions, counterfactual posterior exercises or subsample estimates. The entry documents published estimation evidence but contains no estimator or sampler.

## Conventions and representation

Some differences are transformations, not economic departures:

- The code stores `NU=−ξ` and `NU1=−ξ′`. Comparing the raw signs without that mapping would create a false disagreement.
- The code multiplies the inflation-objective innovation/state by 100 and divides the state by 100 in the policy rule (lines 111 and 316). The entry uses natural-log units. After conversion the original SD is 0.00034, rather than 0.034; it still differs from the paper's 0.0004.
- Fixed land, material demand and one bond position are algebraically eliminated in the code. Their economic restrictions remain. The paper's 36-equation system, code's 50 endogenous variables and entry's 46 variables have different auxiliary-variable choices; these counts do not establish a model difference.
- The code mixes nonlinear expressions in stationary log quantities with linear price/wage equations, and asks Dynare for order one. The paper also describes detrending and linearisation (p.163). The entry stores the first-order equations directly. The original programme does not establish a fully nonlinear higher-order representation.

There is also a small growth convention difference that should be preserved explicitly. The paper defines technology trends using log(1+γ) and reports additive net-growth formulas (12)–(15), pp.133–134. The numerical code exponentiates weighted `TREND_*` coefficients, treating them as log growth (lines 133–142). The entry follows this exponential convention. These agree to first order in small growth rates; they are not exact arithmetic identities at the same numerical γ values.

## Data and observation scope

The paper estimates ten quarterly US observables over 1965Q1–2006Q4 and specifies two measurement errors, for construction hours and construction wage inflation. The reference data file contains ten 168-observation transformed vectors, consistent with that length, but supplies no explicit dates, original raw vintage or complete data-construction recipe. This is a provenance limitation; it does not establish that the observations are incorrect.

The Dynare code supplies concrete observation relations: household-weighted sector hours, sums of household wage levels before calculating nominal wage inflation, and a common trend for aggregate business investment (lines 359–374 and 501–505). The paper explains concepts and transformations, including the aggregate investment trend approximation in footnote 16, but does not fully pin down every computational aggregation in the printed appendix. Those extra code conventions should not be described as independently verified paper identities. The entry documents them as reference conventions; it does not rerun the original data preparation or estimate the model.

The numerical model advertises Dynare 4.0.4 and MATLAB 7.6, while the accompanying steady-state routine uses a later Dynare interface. This is a software-version distinction; it does not establish an economic discrepancy. The steady-state routine computes stationary positive levels algebraically and returns their logs, whereas this entry uses zero log deviations around those levels.

## How much do the economic changes matter?

A controlled comparison holds the numerical-reference parameter values and innovation SDs fixed and changes habit timing and utilisation accounting together. Across nine shocks, six standard output series and 20 quarters, the largest absolute difference in saved one-SD responses is **0.0011308125 log units**, approximately **0.113 percentage points of response**. It occurs in business investment two quarters after an investment-specific technology innovation: the original response is approximately **1.6655%**, versus **1.5524%** in the reconciled equations.

This comparison excludes the effect of changing to published posterior means and does not isolate each equation adjustment separately. It is not a distance from the paper's reported posterior results, and it is not a maximum over every model variable. Agreement between the repository and the separately reconciled Dynare case validates their numerical consistency under the stated interpretation; it does not resolve the publication's internal ambiguities or verify unchanged author code.

## Source references

- Iacoviello, M., and S. Neri (2010). Housing Market Spillovers: Evidence from an
  Estimated DSGE Model. *American Economic Journal: Macroeconomics* 2(2), 125–164.
  [doi:10.1257/mac.2.2.125](https://doi.org/10.1257/mac.2.2.125). Utilities p.128;
  footnote 15 p.132; resource equation and growth pp.133–134; Tables 3–4 and
  footnote 26 pp.139–140; Appendix A pp.158–159; B1 p.159; B4/B5/B9/B10 p.160;
  wage slopes, B33/B34 and costs p.162; approximation p.163.
- Numerical reference identified by the SHA-256 above: scope lines 24–25;
  coefficients and switches 59–121; growth 133–142; budget 220–222; capital
  conditions 232–241; policy 314–316; habits 325–330; wages 334–350;
  utilisation 355–356; observations 359–374; priors and estimation 453–523.
- [Structured estimation reference](../estimation.yaml): full published tables,
  original numerical-reference coefficients and estimation options.
- [Reusable consumption and capital derivations](../../../docs/theory/consumption-and-capital.md#in-capital-adjustment),
  [resource accounting](../../../docs/theory/two-sector-housing-production.md#aggregation)
  and [wage setting](../../../docs/theory/wage-setting.md#in-sectoral-wages).
- [Independent reference conventions](../../../tests/fixtures/README.md): source
  identification, economic adjustments, shock normalisation and response units.
  The committed numerical fixture uses article means. The controlled comparison
  above instead holds the numerical reference's own coefficients and shock SDs
  fixed, uses both unmodified and reconciled equations, and takes the maximum
  absolute difference across `data_CC,data_IK,data_IH,data_QQ,zata_GDP,data_RR`,
  nine innovations and horizons 0–19. Its value is a point-profile comparison,
  rather than a published empirical estimate.
