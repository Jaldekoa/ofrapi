from ofrapi.fsi import financial_stress_index
import pandas as pd


def test_financial_stress_index():
    assert isinstance(financial_stress_index(), pd.DataFrame)

