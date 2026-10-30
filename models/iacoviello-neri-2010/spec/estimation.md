# Bayesian estimation reference: Iacoviello and Neri (2010)

The paper estimates a housing and collateral DSGE model on quarterly US data,
**1965Q1–2006Q4**, using ten observables. The posterior tables and estimation
method are part of the canonical scientific reference. Values in
[`../estimation.yaml`](../estimation.yaml) are **published reference evidence**,
not an estimation performed by this repository.

The primary source is Iacoviello and Neri (2010), *American Economic Journal:
Macroeconomics* 2(2), 125–164,
[doi:10.1257/mac.2.2.125](https://doi.org/10.1257/mac.2.2.125).
Section II, printed pp. 134–140 (one-based physical PDF pp. 10–16), describes
estimation; Appendix A, printed pp. 158–159 (PDF pp. 34–35), lists data sources.

## Observables, trends and units

The real series are consumption, residential investment, business investment and
house prices. Consumption and both investments are per capita. The remaining
observables are the nominal short rate, goods inflation, hours in each sector and
nominal wage inflation in each sector. Real series enter in log levels with
initial level information removed and deterministic trends retained. Inflation,
interest rates, hours and wage inflation are demeaned. The short rate and inflation
are quarterly. Natural logs are used; multiplying by 100 gives percentage units.

Let $\widehat C_t,\widehat{IH}_t,\widehat{IK}_t,\widehat q_t$ be stationary model
log deviations, with normalisation constants suppressed because levels are
removed. The four trending observable equations are

$$
\begin{bmatrix}C^{obs}_t\\IH^{obs}_t\\IK^{obs}_t\\q^{obs}_t\end{bmatrix}
=\begin{bmatrix}\log G_C\\\log G_H\\\log G_K\\\log G_q\end{bmatrix}t
+\begin{bmatrix}\widehat C_t\\\widehat{IH}_t\\\widehat{IK}_t\\\widehat q_t\end{bmatrix}.
$$

The paper assigns aggregate business investment the trend of nonhousing-sector
capital because construction capital is a small part of the aggregate
(footnote 16, printed p. 133, PDF p. 9). This is a measurement convention;
construction capital itself grows with consumption. Stationary aggregate
consumption and business investment are steady-state weighted log aggregations
of household consumption and sectoral capital accumulation.

The stationary rate equations are

$$
R_t^{obs}=i_t,\qquad \pi_t^{obs}=\pi_t.
$$

For sector $s=c,h$, let $n_s=\alpha_pn_{ps}+(1-\alpha_p)n_{bs}$ denote the
model labour composite, and let $\omega_s$ be the log change in the aggregate
nominal wage. Then

$$
n_c^{obs}=n_c,\qquad n_h^{obs}=n_h+e_{nh},
$$

$$
\omega_c^{obs}=\omega_c,\qquad\omega_h^{obs}=\omega_h+e_{wh}.
$$

The numerical reference aggregates the two household wage levels before taking
the log difference: if $\bar W_{js}$ are their stationary wage levels, the
linear wage deviation is
$w_s=\sum_j[\bar W_{js}/\sum_j\bar W_{js}]w_{js}$ and
$\omega_s=w_{s,t}-w_{s,t-1}+\pi_t$ after demeaning trend wage inflation.
These wage weights differ from the fixed household labour-income weights used
for the production labour composite. They are explicit reference observation
conventions, rather than an identity proved by the printed Appendix A.

Only construction hours and construction wage inflation have measurement errors.
They represent measurement limitations discussed on printed p. 136 (PDF p. 12),
including incomplete coverage of self-employment in construction and divergence
between available industry wages and consumption trends. The two measurement
innovations are separate from the nine structural shocks. Ten observables do not
imply ten structural disturbances.

## Data concepts and limitations

Appendix A identifies BEA real personal consumption expenditure, private
nonresidential fixed investment and private residential fixed investment from
table 1.1.6, chained 2000 dollars, divided by BLS civilian noninstitutional
population. The empirical consumption aggregate includes housing services and
durables, while the theoretical aggregate excludes them. Footnote 18 explains
that the available chained aggregate is used to retain a broad consumption measure.

The Census constant-quality new-house price includes land and is deflated by the
BLS nonfarm-business implicit deflator. Goods inflation is the quarterly log
change in that deflator. The short rate is the three-month Treasury bill
secondary-market rate in quarterly units. Hours use payroll employment times
average weekly hours, divided by population. Wage inflation uses nominal hourly
earnings of production/nonsupervisory workers in total private nonfarm payrolls
and construction. Exact series identifiers are recorded in `estimation.yaml`.

These sources define the empirical concepts but do not recover the original data
vintage, revisions, seasonal aggregation choices or every initial-level alignment.
A data vector with the right dimension alone does not establish empirical
replication. The separately referenced Web Appendices C/D contain additional
estimation and robustness material beyond the printed article and Appendices A/B.

## Likelihood and posterior computation

The authors detrend and linearise the equilibrium around its balanced-growth
steady state. Given parameters, the first-order solution defines a linear
state-space representation. The likelihood combines the model state transition,
ten-observable measurement system, nine independent structural innovations and
two measurement errors. Bayesian inference satisfies

$$
p(\theta\mid D)\propto p(D\mid\theta)p(\theta).
$$

The priors in Tables 3–4 are parameterised by the stated **means and standard
deviations**. Footnote 26, printed pp. 139–140 (PDF pp. 15–16), describes a
random-walk Metropolis sampler, Gaussian jumps based on posterior curvature at
the maximum, **500,000 draws**, a scale chosen for approximately **25 percent
acceptance**, and convergence checks comparing moments from the two halves of
the draws. The printed article does not specify a numerical proposal scale or
burn-in count. Additional details belong to Web Appendix C; they are not inferred
from a separate numerical programme.

The reference programme instead requests 5,000 MH repetitions, proposal scale
0.2, one block, four presample observations and its own likelihood initialisation.
Its housing-technology persistence prior has SD 0.09, while Table 4 states 0.10.
Those are distinct reference settings and must not replace the publication's
reported method. The original authors describe that programme as reproducing
some basic findings, rather than as the complete original estimation system.

## Fixed parameters, priors and posterior evidence

Table 1, printed p. 137 (PDF p. 13), fixes the two discount factors,
housing utility weight, four factor shares, three depreciation rates, price and
wage markups, LTV and inflation-objective persistence. Table 2, p. 138
(PDF p. 14), reports rounded steady ratios conditional on calibration and
estimated parameters. It gives expenditure shares of 67 percent consumption,
27 percent business investment and 6 percent residential investment, and housing
wealth of 1.36 times annual GDP.

Table 3, printed p. 139 (PDF p. 15), contains 22 estimated structural quantities:
two habits, two labour elasticities, two sector-mobility parameters, two capital
adjustment coefficients, the patient income share, three policy coefficients,
six Calvo/indexation coefficients, utilisation curvature and three technology
trends. Technology growth is reported as $100\gamma_A$, so a posterior mean
0.32 corresponds to net growth 0.0032 in the consumption technology parameter.

Table 4 on the same page contains six estimated shock persistences and eleven
innovation standard deviations, of which nine are structural and two are
measurement errors. The inflation-objective persistence is calibrated separately
at 0.975. The cost-push and monetary innovations have no estimated AR coefficient.
Beta priors are used for persistence, normal and gamma or beta priors for
structural quantities, and inverse-gamma priors for all innovation SDs. The
machine-readable tables retain every prior, posterior **mean**, **median**,
**2.5th percentile** and **97.5th percentile**. They contain no invented posterior
mode.

The posterior patient labour-income share is 0.79, implying a constrained share
of 0.21. Habits are larger for borrowers (0.58) than for patients (0.32).
Housing-sector wages are more sticky (0.91) than nonhousing wages (0.79), while
price stickiness is 0.83. These are rounded published posterior means. Numerical
reference values such as the policy inflation response 1.40444 differ from the
published mean 1.44; they are not merely the same estimates at higher precision.

## Parameter profiles and empirical claims

The canonical numerical defaults use Table 3–4 posterior means at published
precision. The separately named reference-code parameter profile allows controlled
comparisons while retaining the primary-source habit derivative, sector-correct
wage slopes and budget-consistent net utilisation accounting described in
[the model specification](model.md). Comparing an unmodified reference programme
also measures equation differences, especially for the intertemporal preference
and utilisation channels.

Inflation-objective innovation scaling needs particular care: the reference state
is scaled by 100 and divided by 100 in its policy equation. Its raw innovation
SD is therefore 100 times the unscaled published SD. Parameter transformations
must change both coefficients and SDs together. The sign change `NU=-xi` is
another explicit normalisation.

Sections III–IV report impulse responses, variance decompositions, historical
contributions and collateral counterfactuals. Housing demand raises prices and
construction; housing technology raises construction while lowering prices;
monetary tightening depresses housing activity. The authors find nonnegligible
consumption spillovers from housing collateral and greater spillovers in the
later subsample. The subsample windows are 1965Q1–1982Q4 and 1989Q1–2006Q4.
Those posterior-dependent findings remain published reference evidence. Fixed-
parameter first-order responses do not reproduce their uncertainty bands,
smoothed shock histories, subsample posteriors or reported variance shares.
