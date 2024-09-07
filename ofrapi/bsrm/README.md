# Bank Systemic Risk Monitor
The OFR Bank Systemic Risk Monitor (BSRM) is a collection of key measures for monitoring systemic risks posed by the largest banks. These include systemic importance scores for international and U.S. banks, the OFR’s Contagion Index, and other common measures of systemic risk.

## Basel Scores
The Basel Committee on Banking Supervision, a group of international bank supervisors, utilizes a set of financial indicators to identify global systemically important banks (G-SIBs). A G-SIB is a bank whose failure could pose a threat to the international financial system. A bank designated as a G-SIB must hold more risk-based capital to enhance its resilience and is subject to additional regulatory oversight.
G-SIB scores are calculated by averaging the following five categories of the Basel Committee's assessment methodology: size, interconnectedness, substitutability, complexity, and cross-jurisdictional activity.
The calculated G-SIB scores and supervisory judgment determine the size of the capital add-on, or surcharge, which is shown in the legend. Banking regulators may require capital surcharges that are calculated using a different methodology. See U.S. G-SIB Surcharges for the Federal Reserve methodology applicable to U.S. G-SIBs.

### basel_scores

```python
from ofrapi.bsrm import basel_scores
df = basel_scores()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing the Basel scores from a set of financial indicators to identify global systemically important banks (G-SIBs).


## U.S. G-SIB Surcharges
U.S. G-SIBs are banks whose failure could pose a threat to the financial system. A U.S. G-SIB must hold more risk-based capital than a non-G-SIB. The size of the capital add-on, or surcharge, is calculated using two different methods. The higher of the two surcharges applies. The surcharges are shown in the legend.
- The first method is based on the Basel Committee framework.
- The second method (Method II) uses similar inputs to the first, but replaces the measure of substitutability with a measure of short-term wholesale funding. The Method II scores are calculated by summing the following five categories of the Federal Reserve Board’s assessment methodology: size, interconnectedness, complexity, cross-jurisdictional activity, and short-term wholesale funding.
For foreign banks, the data presented are limited to the activities of the U.S. operations.

### us_systemic_scores

```python
from ofrapi.bsrm import us_systemic_scores
df = us_systemic_scores()
```
#### Returns
- `pd.DataFrame`: A DataFrame containing the U.S. G-SIB Surcharges data.


## OFR Contagion Index
The OFR’s Contagion Index measures the loss that could spill over to the rest of the financial system if a given bank were to default. It depends on the size of the bank, its leverage, and how connected it is to other financial institutions:

```terminal
OFR Contagion Index = Connectivity X Net Worth X (Outside Leverage - 1).
```

For foreign banks, the data presented are limited to the activities of the U.S. operations.

### get_contagion_index

```python
from ofrapi.bsrm import contagion_index
df = contagion_index()
```
#### Returns
- `pd.DataFrame`: A DataFrame containing the OFR’s Contagion Index data.


## Assets/Equity/Leverage
Total assets, total equity, and leverage are common measures used to gauge systemic risk.
For foreign banks, the data presented are limited to the activities of the U.S. operations.

### assets_equity_leverage

```python
from ofrapi.bsrm import assets_equity_leverage
df = assets_equity_leverage()
```
#### Returns
- `pd.DataFrame`: A DataFrame containing total assets, total equity, and leverage data.

## Short-term Wholeslae Funding
A bank's reliance on short-term wholesale funding increases its exposure to liquidity and funding risk. Three measures of a bank’s use of short-term wholesale funding are:
The **Short-Term Funding Metric (STF-RWA)** is the percentage of a bank’s short-term wholesale funding amount (STFA) to its average risk-weighted assets (RWA).
The **Short-Term Funding Dependence (STF-Dependence)** refers to the percentage of a bank’s STFA to its total liabilities.
The **Short-Term Funding Coverage (STF-Coverage)** compares the percentage of a bank’s STFA amount to its average weighted high-quality liquid assets (HQLA).
For foreign banks, the data presented are limited to the activities of the U.S. operations.

### short_term_wholesale_funding

```python
from ofrapi.bsrm import short_term_wholesale_funding
df = short_term_wholesale_funding()
```
#### Returns
- `pd.DataFrame`: A DataFrame containing a bank’s use of short-term wholesale funding data.
