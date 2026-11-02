# Theory

Where the algebra behind the components lives.

The component files under `components/` carry the equations the solver uses, each with a
`status` saying what it is with respect to the cited work and, where the status is
`derived` or `adapted`, a `derivation` pointing into one of the documents here. The
documents are the single source of truth for the steps: a component does not restate
them, and no derivation is maintained in two places.

| document | covers | components |
|---|---|---|
| [`price-setting.md`](price-setting.md) | Dixit–Stiglitz and Kimball aggregation, the firm's reset problem, the price index, the Calvo and indexed Phillips curves, Rotemberg and its first-order equivalence, housing-model growth discounting | `calvo-prices`, `calvo-prices-domestic`, `calvo-prices-kimball`, `price-indexation`, `rotemberg-prices`, `calvo-prices-indexation-in` |
| [`wage-setting.md`](wage-setting.md) | differentiated labour, the wage markup, staggered wage setting, the real wage gap identity, marginal cost under sticky wages, household and sector-specific wage equations | `calvo-wages`, `calvo-wages-kimball`, `wage-indexation`, `sectoral-calvo-wages-in` |
| [`consumption-and-capital.md`](consumption-and-capital.md) | internal and external habits, the Euler equation and the marginal rate of substitution, utilisation, investment-flow and capital-stock adjustment costs, Tobin's q, accumulation and trend growth | `habit-consumption`, `capital-utilisation`, `investment-adjustment-cost`, `core-nk-medium`, `internal-habit-consumption-in`, `capital-stock-adjustment-in`, `sectoral-capital-utilisation-in` |
| [`open-economy.md`](open-economy.md) | relative prices and the two inflation rates, the real exchange rate, international risk sharing, openness in the IS curve and in natural output, the four monetary regimes | `core-soe-gm`, `calvo-prices-domestic`, the four `rule-*` components of that family |
| [`housing-and-collateral.md`](housing-and-collateral.md) | heterogeneous-household budgets, internal housing services, collateral, debt timing and fixed-land valuation | `core-housing-in`, `housing-collateral-in` |
| [`two-sector-housing-production.md`](two-sector-housing-production.md) | sectoral production, materials, budget-consistent resource aggregation, GDP and balanced growth | `core-housing-in`, `taylor-rule-in` |
| [`source-editions.md`](source-editions.md) | Primary references, checked equation numbering, scientific provenance boundaries and explicit source limitations | All canonical entries |

The mechanism-derivation documents include a table headed **what a transplant requires**. That table is the
part written for reuse rather than for reading: it says which steps of the derivation
fail when the environment changes, so that an equation is not carried into a model whose
primitives no longer support it.

## How to read a `derivation` pointer

A pointer has the form `docs/theory/<file>.md#<anchor>`. The anchor is a label the
document declares in place, as a line reading **Anchor: `<name>`**. `tests/test_knowledge_base.py`
checks that every pointer resolves to a declared anchor, so a derivation cannot be
renamed or removed while a component still points at it.

## What these documents are not

They are not a textbook, and they do not derive what the library does not use. They also
do not claim more than has been established: where a step is reproduced in outline only,
or where a normalisation is the source's rather than a result, the text says so at that
point. Section 5 of `price-setting.md` and sections 3 and 4.2 of
`consumption-and-capital.md` are the three places that applies.
