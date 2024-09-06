from ofrapi import __get_worksheet_from_url


def get_basel_scores():
    """
    Returns a Basel scores from a set of financial indicators to identify global systemically important banks (G-SIBs).

    Return:
        pd.DataFrame: A DataFrame containing the data.
    """
    return __get_worksheet_from_url(sheet_name="Basel Scores")


def get_us_systemic_scores():
    """
    Returns a U.S. G-SIB Surcharges data.

    Return:
        pd.DataFrame: A DataFrame containing the data.
    """
    return __get_worksheet_from_url(sheet_name="US Systemic Scores")


def get_contagion_index():
    """
    Returns the OFR's Contagion Index.

    Return:
        pd.DataFrame: A DataFrame containing the data.
    """
    return __get_worksheet_from_url(sheet_name="Contagion")


def get_leverage():
    """
    Returns total assets, total equity, and leverage data that are common measures used to gauge systemic risk.

    Return:
        pd.DataFrame: A DataFrame containing the data.
    """
    return __get_worksheet_from_url(sheet_name="Leverage")


def get_short_term_wholesale_funding():
    """
    Returns short-term wholesale funding data.

    Return:
        pd.DataFrame: A DataFrame containing the data.
    """
    return __get_worksheet_from_url(sheet_name="Short-term Wholesale Funding")
