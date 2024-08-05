from ofrapi import __series_timeseries, __calc_spread
from ofrapi.hfm import __api

__all__ = ["series_timeseries", "calc_spread"]


def series_timeseries(mnemonic, **query):
    """
    Returns the series for the given mnemonic as a list of date/value pairs. Each mnemonic is required to have an aggregation series and that is the default subseries returned. You can specify a different subseries to return.

    Args:
        mnemonic (str): **This parameter is required**. The unique identifier for the series for which you want to retrieve data.

    Keyword Args:
        label (str): The specific subseries to return. Possible labels are: "aggregation" and "disclosure_edits". By default the "aggregation" subseries is returned.
        start_date (str): First date in "YYYY-MM-DD" format for which you want to receive data. If no start_date is given, "1901-01-01" is used.
        end_date (str): Last date in "YYYY-MM-DD" format for which you want to receive data. If no end_date is given, today's date is used.
        periodicity (str): Converts the series to the given periodicity. Available values are: ["A", "AS", "D", "M", "MS", "W", "B", "BM", "BMS", "Q", "BQ", "QS", "BQS", "BA", "BAS"]
        how (str): How to calculate the value for the given periodicity. By default the last value in that period is given. Available values are: ["first", "last", "mean", "median", "sum"]
        remove_nulls (str): If this parameter is set to "true" all nulls in the series will be removed.
        time_format (str): The format for the dates in the series. By default they are returned as strings in the format: YYYY-MM-DD. Available values are: ["date", "ms"]


    Return:
        pd.DataFrame: A DataFrame containing the timeseries data.
    """
    return __series_timeseries(__api, mnemonic, **query)


def calc_spread(x: str, y: str, **query):
    """
    Returns the difference between the data points of two specified series. It will compute the spread of the aggregation subseries by calculating the difference between the first mnemonic (x) and the second mnemonic (y).

    Args:
        x (str): **This parameter is required**. The mnemonic (unique identifier) for the first series that you want to use as the base of the calculation.
        y (str): **This parameter is required**. The mnemonic (unique identifier) for the second series that will be subtracted from x.

    Keyword Args:
        start_date (str): First date in "YYYY-MM-DD" format for which you want to receive data. If no start_date is given, "1901-01-01" is used.
        end_date (str): Last date in "YYYY-MM-DD" format for which you want to receive data. If no end_date is given, today's date is used.
        periodicity (str): Converts the series to the given periodicity. Available values are: ["A", "AS", "D", "M", "MS", "W", "B", "BM", "BMS", "Q", "BQ", "QS", "BQS", "BA", "BAS"]
        how (str): How to calculate the value for the given periodicity. By default, the last value in that period is given. Available values are: ["first", "last", "mean", "median", "sum"]
        remove_nulls (str): If this parameter is set to "true" all nulls in the series will be removed.
        time_format (str): The format for the dates in the series. By default, they are returned as strings in the format: YYYY-MM-DD. Available values are: ["date", "ms"]


    Return:
        pd.DataFrame: A DataFrame containing the spread between two timeseries data.
    """
    return __calc_spread(__api, x, y, **query)
