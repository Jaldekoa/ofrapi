from ofrapi.bsrm import basel_scores, us_systemic_scores, contagion_index, assets_equity_leverage, short_term_wholesale_funding
import pandas as pd


def test_basel_scores():
    assert isinstance(basel_scores(), pd.DataFrame)


def test_us_systemic_scores():
    assert isinstance(us_systemic_scores(), pd.DataFrame)


def test_contagion_index():
    assert isinstance(contagion_index(), pd.DataFrame)


def test_assets_equity_leverage():
    assert isinstance(assets_equity_leverage(), pd.DataFrame)


def test_short_term_wholesale_funding():
    assert isinstance(short_term_wholesale_funding(), pd.DataFrame)

