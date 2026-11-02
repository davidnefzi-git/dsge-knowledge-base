# Two-sector production, aggregation and balanced growth

Iacoviello and Neri (2010), equations (6)–(15) and Appendix B,
*American Economic Journal: Macroeconomics* 2(2), 125–164,
[doi:10.1257/mac.2.2.125](https://doi.org/10.1257/mac.2.2.125), is the primary
reference. Relevant printed pages are 131–134 and 161–163
(one-based physical PDF pp. 7–10 and 37–39).

## Production primitives

### Production

**Anchor: `production`.**

Let $L_{s,t}=n_{ps,t}^{\alpha_p}n_{bs,t}^{1-\alpha_p}$ and
$\nu_h=1-\mu_h-\mu_l-\mu_b$. The technologies are

$$
Y_t=(A_{ct}L_{c,t})^{1-\mu_c}(z_{ct}k_{c,t-1})^{\mu_c},
$$

$$
IH_t=(A_{ht}L_{h,t})^{\nu_h}k_{bt}^{\mu_b}
(z_{ht}k_{h,t-1})^{\mu_h}l_{t-1}^{\mu_l}.
$$

Capital is predetermined; utilisation is chosen within the period. Nonhousing
output is transformed into consumption, capital and construction materials.
Construction has flexible output prices and uses fixed aggregate land $l_t=1$.
Patient and borrower labour are complementary within each sector, with constant
income weights $\alpha_p$ and $1-\alpha_p$.

### Factor demands

**Anchor: `factor-demands`.**

Competitive wholesale nonhousing firms sell to retailers at relative price $1/X_t$.
Their factor conditions are

$$
w_{pc,t}n_{pc,t}=\frac{\alpha_p(1-\mu_c)Y_t}{X_t},
\quad w_{bc,t}n_{bc,t}=\frac{(1-\alpha_p)(1-\mu_c)Y_t}{X_t},
$$

$$
R_{ct}z_{ct}k_{c,t-1}=\frac{\mu_cY_t}{X_t}.
$$

Construction has no retail markup:

$$
w_{ph,t}n_{ph,t}=\alpha_p\nu_hq_tIH_t,
\quad w_{bh,t}n_{bh,t}=(1-\alpha_p)\nu_hq_tIH_t,
$$

$$
R_{ht}z_{ht}k_{h,t-1}=\mu_hq_tIH_t,
\quad R_{lt}l_{t-1}=\mu_lq_tIH_t,
\quad p_{bt}k_{bt}=\mu_bq_tIH_t.
$$

The patient material optimum B8 gives $p_{bt}=1$. Substituting
$k_{bt}=\mu_bq_tIH_t$ into the construction technology eliminates materials:

$$
(1-\mu_b)\widehat{IH}_t=
\nu_h\widehat A_{ht}+\nu_h[\alpha_p\widehat n_{ph,t}+
(1-\alpha_p)\widehat n_{bh,t}]+\mu_b\widehat q_t+
\mu_h(\widehat z_{ht}+\widehat k_{h,t-1}).
$$

Land has zero quantity deviation but retains its level share. Omitting $\mu_l$
from $\nu_h$ after eliminating land would alter the production function.

## Market clearing and expenditure aggregation

### Aggregation

**Anchor: `aggregation`.**

Define $C_t=c_{pt}+c_{bt}$,
$IK_{c,t}=k_{ct}-(1-\delta_{kc})k_{c,t-1}$ and
$IK_{h,t}=k_{ht}-(1-\delta_{kh})k_{h,t-1}$. Full resource accounting gives

$$
C_t+\frac{IK_{c,t}}{A_{kt}}+IK_{h,t}+k_{bt}+\phi_t+
\frac{a_c(z_{ct})k_{c,t-1}}{A_{kt}}+a_h(z_{ht})k_{h,t-1}=Y_t.
$$

The displayed goods-clearing condition B34 omits the last two terms even though
B1 includes them. Summing household budgets and firm income restores these
utilisation resource costs. Their first-order coefficients are nonzero because
$a_s'(1)\ne0$. The canonical accounting closure retains them. Quadratic capital
adjustment costs have zero level and first derivative on the balanced-growth path,
so their direct resource contribution vanishes at first order.

For stationary levels, write $\bar k_c/G_K$ and $\bar k_h/G_C$ for lagged physical
stocks. The first-order resource contribution of utilisation is

$$
\frac{\bar R_c\bar k_c}{G_K}\widehat z_{ct}
+\frac{\bar R_h\bar k_h}{G_C}\widehat z_{ht},
$$

where the consumption-sector rental is consistent with the stationary price of
capital. Consumption and investment terms must use the same growth and price
normalisation before these coefficients are evaluated.

Housing clearing is

$$
h_{pt}+h_{bt}-(1-\delta_h)(h_{p,t-1}+h_{b,t-1})=IH_t.
$$

Stationarisation divides lagged stocks by $G_H$; log-linear coefficients use each
household's steady housing stock. Loan clearing is $b_t+b'_t=0$ and land clearing
is $l_t=1$.

GDP in the monetary rule uses fixed balanced-growth expenditure prices:
$GDP_t=C_t+IK_t+\bar q_tIH_t$. Thus short-run changes in $q_t$ do not mechanically
enter real GDP growth. Its first-order log deviation is the sum of consumption,
business investment and residential investment deviations weighted by their
steady expenditure shares. Appendix B33 also gives the production-side expression
$Y_t-k_{bt}+\bar q_tIH_t$. With utilisation resource costs retained, this expression
includes those costs and differs from final expenditure. The policy statistic here
selects the expenditure definition in footnote 15. Both definitions exclude imputed
housing rents. Goods output $Y_t$, residential
investment $IH_t$, and expenditure-weighted GDP are distinct quantities.

The monetary rule in quarterly log deviations is

$$
i_t=\rho_i i_{t-1}+(1-\rho_i)
[\phi_\pi\pi_t+\phi_g(y_t-y_{t-1})]+u_{Rt}-s_t.
$$

A positive persistent inflation-objective disturbance lowers the policy rate
conditional on inflation and growth. The unscaled state satisfies
$s_t=\rho_s s_{t-1}+u_{st}$; no factor of 100 belongs to its economic definition.

## Balanced growth and stationary quantities

### Balanced growth

**Anchor: `balanced-growth`.**

The deterministic technology processes are
$A_{st}=(1+\gamma_{As})^tZ_{st}$ for $s=c,h,k$, with stationary AR(1)
$\log Z_{st}=\rho_s\log Z_{s,t-1}+u_{st}$.
The paper states the growth identities (12)–(15) to first order in net rates:

$$
g_C=g_{Kh}=\gamma_{AC}+\frac{\mu_c}{1-\mu_c}\gamma_{AK},
\qquad g_{Kc}=\gamma_{AC}+\frac{1}{1-\mu_c}\gamma_{AK},
$$

$$
g_H=(\mu_h+\mu_b)g_C+\nu_h\gamma_{AH},
\qquad g_q=g_C-g_H.
$$

The computational convention treats the small reported technology trend rates as
log-growth coefficients $a_s=\gamma_{As}$ and defines

$$
\log G_C=a_c+\frac{\mu_c}{1-\mu_c}a_k,
\quad \log G_K=a_c+\frac{a_k}{1-\mu_c},
$$

$$
\log G_H=(\mu_h+\mu_b)\log G_C+\nu_ha_h,
\quad \log G_q=\log G_C-\log G_H.
$$

Then $G_qG_H=G_C$ and $G_K/G_C=\exp(a_k)$ exactly. This exponential convention
matches the numerical reference and the paper's net-growth identities to first
order in the small trend rates. It is an explicit approximation convention:
$\exp(\gamma_A)$ differs from $1+\gamma_A$ beyond first order. Both named
parameter profiles use this convention. Their differences reflect different
point values, rather than a change of trend formula.

Divide consumption, goods output, debt, construction-sector capital, material inputs
and real wages by $G_C^t$; nonhousing capital by $G_K^t$; housing quantities and
residential investment by $G_H^t$; house prices by $G_q^t$. Marginal consumption
utilities scale inversely with $G_C^t$. Inflation, interest rates, utilisation and
hours are stationary. A lagged stationary capital or housing stock therefore
enters divided by its own gross growth rate.

Patient bond optimality gives $\bar R=1/\beta_p$ under unit trend inflation. Unit
utilisation gives

$$
\bar R_c=\frac{G_K/G_C}{\beta_p}-(1-\delta_{kc}),
\qquad \bar R_h=\beta_p^{-1}-(1-\delta_{kh}),
$$

with the stationary consumption-sector price of capital normalised to one.
Steady investments are $\bar{IK}_c=[1-(1-\delta_{kc})/G_K]\bar k_c$ and
$\bar{IK}_h=[1-(1-\delta_{kh})/G_C]\bar k_h$; residential investment is
$[1-(1-\delta_h)/G_H](\bar h_p+\bar h_b)$.

## What a transplant requires

| Change | Consequence |
| --- | --- |
| Different capital ownership or timing | Re-derive factor payments, household returns and growth-adjusted lag coefficients. |
| Endogenous land | Restore its quantity in housing supply and solve the land market. |
| Different material-input price | Restore its optimality and factor-demand equations. |
| Current house-price GDP weights | Change the policy statistic and its response to housing shocks. |
| Stochastic technology trends | Replace deterministic detrending and reconsider the stationary state vector. |
| National-accounts consumption excluding housing services | Reconstruct the empirical series and its observable relation; the published broad series is not identical. |
