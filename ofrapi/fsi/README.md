# Financial Stress Index
The OFR Financial Stress Index (OFR FSI) is a daily market-based snapshot of stress in global financial markets. It is constructed from 33 financial market variables, such as yield spreads, valuation measures, and interest rates. The OFR FSI is positive when stress levels are above average, and negative when stress levels are below average.

The OFR FSI incorporates five categories of indicators: credit, equity valuation, funding, safe assets and volatility. The FSI shows stress contributions by three regions: United States, other advanced economies, and emerging markets.

### financial_stress_index

```python
from ofrapi.fsi import financial_stress_index
df = financial_stress_index()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing the OFR Financial Stress Index with categories and region factors.


