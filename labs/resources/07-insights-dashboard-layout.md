# 07 Insights Dashboard — Layout Guide

Create `C695-campaign-pack/07-insights-dashboard.xlsx` with these three tabs. The workbook—not a CSV—is the primary deliverable.

## Raw

Import `harbour-hearth-instagram-performance.csv` unchanged. Keep the supplied header in row 1 and the six data rows in rows 2–7. Add no formulas to this tab.

## Calculations

Link columns A–Q to the corresponding Raw cells using formulas. Add these calculated columns beginning in R:

| Column | Header | Row 2 formula pattern |
|---|---|---|
| R | interactions | `=SUM(H2:K2)` |
| S | interaction_rate_by_reach | `=IF(G2=0,NA(),R2/G2)` |
| T | save_rate_by_reach | `=IF(G2=0,NA(),J2/G2)` |
| U | share_rate_by_reach | `=IF(G2=0,NA(),K2/G2)` |
| V | profile_visit_rate_by_reach | `=IF(G2=0,NA(),L2/G2)` |
| W | link_click_rate_by_reach | `=IF(G2=0,NA(),M2/G2)` |
| X | purchase_rate_by_link_click | `=IF(M2=0,NA(),N2/M2)` |
| Y | paid_cpa | `=IF(OR(D2<>"Paid",N2=0),NA(),O2/N2)` |
| Z | paid_roas | `=IF(OR(D2<>"Paid",O2=0),NA(),P2/O2)` |
| AA | validation_status | Enter `PASS` or `DATA ISSUE — <REASON>` after the row checks |

Fill formulas through row 7. Format rates as percentages and spend, revenue, and CPA as Singapore-dollar currency.

## Dashboard

Create KPI cards for the required totals. Beside each value, record the source range or formula. Use these totals-based paid formulas:

- Blended paid CPA = total spend for Paid rows ÷ total purchases for Paid rows.
- Blended paid ROAS = total revenue for Paid rows ÷ total spend for Paid rows.
- Do not average row-level CPA or ROAS.

Add a format comparison table for Image, Carousel, Reel, and Stories. Include mean interaction, save, and share rates; total link clicks; total purchases; and an explicit organic/paid scope note.

Add an exception panel and this Verification Log:

| Check ID | Source row or range | Formula tested | Expected value | Observed value | PASS / REVISE | Reviewer | Date |
|---|---|---|---:|---:|---|---|---|
| V01 | <RANGE> | <FORMULA> |  |  |  |  |  |
| V02 | <RANGE> | <FORMULA> |  |  |  |  |  |
| V03 | <RANGE> | <FORMULA> |  |  |  |  |  |

Minimum visual setup: dark teal section headers, readable wrapped labels, yellow fill for editable notes, green/red status meaning with a text key, frozen header rows, and hidden gridlines where the sections already define structure.
