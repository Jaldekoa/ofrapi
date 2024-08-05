from ofrapi.hfm.get_series_info import *
from ofrapi.hfm.get_series_data import *
from ofrapi.hfm.series_info_data import *
import pandas as pd


# ofrapi.hfm.get_series_info
def test_metadata_mnemonics():
    assert isinstance(metadata_mnemonics(dataset="fpf"), pd.DataFrame)
    assert isinstance(metadata_mnemonics(output="by_dataset"), pd.DataFrame)


def test_metadata_query():
    assert isinstance(metadata_query(mnemonic="fpf-allqhf_cdsup250bps_p5"), pd.DataFrame)
    assert isinstance(metadata_query(mnemonic="fpf-allqhf_cdsup250bps_p5", fields="release/long_name"), pd.DataFrame)


def test_metadata_search():
    assert isinstance(metadata_search(query="Fund*"), pd.DataFrame)
    assert isinstance(metadata_search(query="*credit*"), pd.DataFrame)


# ofrapi.hfm.get_series_data
def test_series_timeseries():
    assert isinstance(series_timeseries(mnemonic="fpf-allqhf_cdsdown250bps_p5"), pd.DataFrame)
    assert isinstance(series_timeseries(mnemonic="fpf-allqhf_cdsdown250bps_p5", periodicity="W", how="mean"), pd.DataFrame)


def test_calc_spread():
    assert isinstance(calc_spread(x="FPF-ALLQHF_CDSDOWN250BPS_P5", y="FPF-ALLQHF_CDSDOWN250BPS_P50"), pd.DataFrame)


# ofrapi.hfm.series_info_data
def test_series_full():
    x, y = series_full(mnemonic="FPF-ALLQHF_NONGSIB_SUM")
    assert isinstance(x, pd.DataFrame) and isinstance(y, pd.DataFrame)

    x, y = series_full(mnemonic="FPF-ALLQHF_FINANCINGLIQUIDTYGT7LE90_PERCENT", start_date="2020-02-01", end_date="2020-02-26")
    assert isinstance(x, pd.DataFrame) and isinstance(y, pd.DataFrame)


def test_series_multifull():
    x, y = series_multifull(mnemonics="FPF-ALLQHF_CDSDOWN250BPS_P5,FPF-ALLQHF_CDSDOWN250BPS_P50")
    assert isinstance(x, pd.DataFrame) and isinstance(y, pd.DataFrame)


def test_series_dataset():
    assert isinstance(series_dataset(), pd.DataFrame)
    assert isinstance(series_dataset(dataset="fpf"), pd.DataFrame)


def test_categories():
    assert isinstance(categories(category="liquidity"), pd.DataFrame)
