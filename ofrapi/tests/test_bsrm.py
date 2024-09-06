from ofrapi.bsrm import get_basel_scores, get_us_systemic_scores, get_contagion_index, get_leverage, get_short_term_wholesale_funding
import pandas as pd


def test_get_basel_scores():
    assert isinstance(get_basel_scores(), pd.DataFrame)


def test_get_us_systemic_scores():
    assert isinstance(get_us_systemic_scores(), pd.DataFrame)


def test_get_contagion_index():
    assert isinstance(get_contagion_index(), pd.DataFrame)


def test_get_leverage():
    assert isinstance(get_leverage(), pd.DataFrame)


def test_get_short_term_wholesale_funding():
    assert isinstance(get_short_term_wholesale_funding(), pd.DataFrame)

