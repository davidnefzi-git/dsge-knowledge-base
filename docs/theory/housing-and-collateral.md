# Housing, heterogeneous households and collateral

This document derives the housing and credit margins in Iacoviello and Neri (2010),
*American Economic Journal: Macroeconomics* 2(2), 125–164,
[doi:10.1257/mac.2.2.125](https://doi.org/10.1257/mac.2.2.125).
The controlling conditions are equations (1)–(5), printed pp. 128–130
(one-based physical PDF pp. 4–6), and Appendix B, printed pp. 159–163
(PDF pp. 35–39). The approximation assumes a locally binding constraint.

## Preferences and assets

Use superscripts $p$ and $b$ for patient and borrowing households. Both groups have
measure one; their economic weights arise through production and wage shares.
For type $j$, let $\beta_j$ be its discount factor, $e_j$ its internal habit and
$N_j=(n_{jc}^{1+\xi_j}+n_{jh}^{1+\xi_j})^{1/(1+\xi_j)}$ its labour aggregate.
Its objective is

$$
E_0\sum_{t=0}^{\infty}(\beta_jG_C)^t z_t
\left[\Gamma_j\log(c_{jt}-e_jc_{j,t-1})+j_t\log h_{jt}
-\frac{\tau_t}{1+\eta_j}N_{jt}^{1+\eta_j}\right].
$$

Here $z_t$ multiplies all period utility, $j_t$ is the housing preference weight and
$\tau_t$ shifts labour disutility. $\Gamma_j=(G_C-e_j)/[G_C(1-\beta_je_j)]$
normalises steady-state consumption marginal utility to $1/c_j$ after detrending.
The internal-habit derivative is derived separately in
[consumption and capital](consumption-and-capital.md#8-iacoviello-and-neri-internal-habits).
In levels, $u^j_{h,t}=z_tj_t/h_{jt}$ and

$$
u^j_{n_s,t}=z_t\tau_tN_{jt}^{\eta_j-\xi_j}n_{js,t}^{\xi_j},
\qquad u^j_{c,t}w_{js,t}=u^j_{n_s,t}X_{w,js,t}.
$$

Positive $\xi_j$ limits substitution of hours across sectors. It does not alter the
Cobb–Douglas income shares across household types in production.

## Full patient budget and its elimination

### Patient budget

**Anchor: `patient-budget`.**

Let $B_t>0$ denote borrower debt and therefore patient lending. With patient labour
and retail dividends collected in $D^p_t$, the full budget is

$$
\begin{aligned}
c_{pt}+\frac{k_{ct}}{A_{kt}}+k_{ht}+k_{bt}+q_th_{pt}+p_{lt}l_t+B_t
={}&\frac{w_{pc,t}n_{pc,t}}{X_{w,pc,t}}+
\frac{w_{ph,t}n_{ph,t}}{X_{w,ph,t}}+D^p_t-\phi_t\\
&+\left[R_{ct}z_{ct}+\frac{1-\delta_{kc}-a_c(z_{ct})}{A_{kt}}\right]k_{c,t-1}\\
&+\left[R_{ht}z_{ht}+1-\delta_{kh}-a_h(z_{ht})\right]k_{h,t-1}
+p_{bt}k_{bt}\\
&+\frac{R_{t-1}B_{t-1}}{\Pi_t}+(p_{lt}+R_{lt})l_{t-1}
+q_t(1-\delta_h)h_{p,t-1}.
\end{aligned}
$$

The paper instead uses patient borrowing $b_t=-B_t$, so the asset term changes
sign. Materials $k_{bt}$ are bought and resold competitively within the period;
$p_{bt}=1$. Nominal loans contracted at $t-1$ repay $R_{t-1}B_{t-1}/\Pi_t$,
not $R_tB_{t-1}/\Pi_t$.

Union profits rebate the difference between gross employer wages and household
receipts. Thus adding labour-union dividends makes net household labour receipts
$w_{js,t}n_{js,t}$. Retail profits are $(1-X_t^{-1})Y_t$ and accrue to patients.
Land rents are $R_{lt}l_{t-1}=\mu_lq_tIH_t$.

The reduced equilibrium retains the borrower budget and goods resource identity.
Together with all other markets these imply the patient budget by Walras' law.
This removes a redundant equation without removing patient ownership of capital,
retail firms and land. Rental income must be treated net of utilisation costs. At
$z_s=1$, $a_s(1)=0$ and $a_s'(1)$ equals the relevant rental cost, so the direct
first-order effect of utilisation in $R_sz_sk_{s,-1}$ cancels the derivative of
$a_s(z_s)k_{s,-1}$. The economy still uses resources for utilisation; its first-order
resource terms are retained when the patient budget is replaced by goods clearing.

## Borrower budget

**Anchor: `borrower-budget`.**

Borrowers own housing and supply both types of labour, but own no productive
capital or land. Combining their wage receipts and union dividends gives

$$
c_{bt}+q_th_{bt}-(1-\delta_h)q_th_{b,t-1}
=w_{bc,t}n_{bc,t}+w_{bh,t}n_{bh,t}+B_t-
\frac{R_{t-1}B_{t-1}}{\Pi_t}.
$$

After detrending, the lagged housing term is divided by $G_H$ and debt repayment
by $G_C$. Their coefficients therefore use stationary wealth and debt ratios,
rather than a no-growth accounting convention. The debt stock is positive in
levels; its logarithmic deviation can take either sign.

## Housing demand, debt and the collateral multiplier

### Housing demand

**Anchor: `housing-demand`.**

Patient housing demand and bond optimality are

$$
u^p_{c,t}q_t=u^p_{h,t}+\beta_pG_CE_t[u^p_{c,t+1}q_{t+1}(1-\delta_h)],
$$

$$
u^p_{c,t}=\beta_pG_CE_t[u^p_{c,t+1}R_t/\Pi_{t+1}].
$$

Housing supplies current utility and a depreciated resale value. The borrower has
an additional collateral service:

$$
u^b_{c,t}q_t=u^b_{h,t}+\beta_bG_CE_t[u^b_{c,t+1}q_{t+1}(1-\delta_h)]
+\lambda_tmE_t[q_{t+1}\Pi_{t+1}/R_t],
$$

$$
u^b_{c,t}=\beta_bG_CE_t[u^b_{c,t+1}R_t/\Pi_{t+1}]+\lambda_t.
$$

These are B2–B3 and B14–B15. The multiplier multiplies the derivative of the
borrowing limit with respect to today's housing stock. It must not be omitted
from the housing Euler equation or replaced by an interest-rate spread.

### Binding collateral

**Anchor: `binding-collateral`.**

The constraint is

$$
B_t\leq mE_t\left[\frac{q_{t+1}h_{bt}\Pi_{t+1}}{R_t}\right],
\qquad \lambda_t\geq0.
$$

The maintained local regime sets the inequality to equality. Its stationary
steady state satisfies $\bar B=mG_q\bar q\bar h_b/\bar R$ and $\bar R=1/\beta_p$.
Because detrended marginal utility grows inversely with consumption, B15 implies

$$
\bar\lambda=\bar u_c^b\left(1-\frac{\beta_b}{\beta_p}\right)>0.
$$

Log-linearisation consequently yields

$$
\widehat B_t=\widehat h_{bt}+E_t\widehat q_{t+1}
+E_t\widehat\Pi_{t+1}-\widehat R_t.
$$

This is a first-order identity around a binding steady state; it does not replace
an expectation of a product by a product of expectations in the nonlinear economy.
Large shocks, slack constraints and changes in the borrowing regime require a
different solution method. Sending the borrower wage share to zero is singular
for log borrower variables and does not define a regular nesting test by itself.

## Land and auxiliary asset prices

### Land elimination

**Anchor: `land-elimination`.**

The full economy contains

$$
u^p_{c,t}p_{lt}=\beta_pG_CE_t[u^p_{c,t+1}(p_{l,t+1}+R_{l,t+1})],
\qquad l_t=1.
$$

Land is fixed in aggregate but earns a scarcity rent and has a nonzero price.
Production implies $R_{lt}=\mu_lq_tIH_t$ at unit land. Its balanced-growth
valuation obeys

$$
\frac{\bar p_l\bar l}{\bar q\overline{IH}}=
\frac{\mu_l\beta_pG_C}{1-\beta_pG_C}.
$$

The reduced system substitutes the land-rent identity, imposes fixed land in
production, and recovers the land price from its Euler equation when needed.
Eliminating the land-price variable preserves the fixed-land restriction and its
effect on construction, while avoiding an asset-pricing auxiliary with no feedback
into the retained quantities. Patient and borrower bonds satisfy $b_t+b'_t=0$.

## What a transplant requires

| Change | Consequence |
| --- | --- |
| Slack collateral constraint | Replace the binding local equations by complementary slackness and a suitable solution method. |
| Endogenous LTV | Re-derive debt and housing margins, and add the policy or shock process for $m_t$. |
| Borrowers hold capital or land | Re-derive both budgets, market clearing and all collateral services. |
| Land supply responds to prices | Retain the land quantity equation and its production contribution; unit fixed land is no longer valid. |
| Different habit or wage-profit ownership | Recompute marginal utilities and household cash flows together. |
