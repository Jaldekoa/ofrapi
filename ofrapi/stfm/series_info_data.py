from ofrapi import __series_full, __series_multifull, __series_dataset
from ofrapi.stfm import __api

__all__ = ["series_full", "series_multifull", "series_dataset"]


def series_full(mnemonic, **query):
    """
    Returns all the data and metadata for the given series. A hashed object is returned with a top-level key of the
    mnemonic.

    Args:
        mnemonic (str): **This parameter is required**. The unique identifier for the series for which you want to retrieve data.

    Keyword Args:
        start_date (str): First date in "YYYY-MM-DD" format for which you want to receive data. If no start_date is given, "1901-01-01" is used.
        end_date (str): Last date in "YYYY-MM-DD" format for which you want to receive data. If no end_date is given, today's date is used.
        periodicity (str): Converts the series to the given periodicity. Available values are: ["A", "AS", "D", "M", "MS", "W", "B", "BM", "BMS", "Q", "BQ", "QS", "BQS", "BA", "BAS"]
        how (str): How to calculate the value for the given periodicity. By default the last value in that period is given. Available values are: ["first", "last", "mean", "median", "sum"]
        remove_nulls (str): If this parameter is set to "true" all nulls in the series will be removed.
        time_format (str): The format for the dates in the series. By default they are returned as strings in the format: YYYY-MM-DD. Available values are: ["date", "ms"]


    Return:
        pd.DataFrame, pd.DataFrame: A tuple of two DataFrames containing the data and metadata for the given series.
    """
    return __series_full(__api, mnemonic, **query)


def series_multifull(mnemonics: str, **query):
    """
    Returns all the data and metadata for all given series. A hashed object is returned with a top-level key of the mnemonic.

    Args: mnemonics (str): **This parameter is required**. The unique identifier for the series for which you want to
    retrieve data.

    Keyword Args:
        start_date (str): First date in "YYYY-MM-DD" format for which you want to receive data. If no start_date is given, "1901-01-01" is used.
        end_date (str): Last date in "YYYY-MM-DD" format for which you want to receive data. If no end_date is given, today's date is used.
        periodicity (str): Converts the series to the given periodicity. Available values are: ["A", "AS", "D", "M", "MS", "W", "B", "BM", "BMS", "Q", "BQ", "QS", "BQS", "BA", "BAS"]
        how (str): How to calculate the value for the given periodicity. By default, the last value in that period is given. Available values are: ["first", "last", "mean", "median", "sum"]
        remove_nulls (str): If this parameter is set to "true" all nulls in the series will be removed.
        time_format (str): The format for the dates in the series. By default, they are returned as strings in the format: YYYY-MM-DD. Available values are: ["date", "ms"]


    Return:
        pd.DataFrame, pd.DataFrame: A tuple of two DataFrames containing the data and metadata for the given series.
    """
    return __series_multifull(__api, mnemonics, **query)


def series_dataset(**query):
    """
    Returns a hash of basic information and all the data for a specific dataset. If no specific dataset is given, then a hash containing only basic information about each data set is returned.

    Keyword Args:
        dataset (str): The specific data set for which to return the underlying series information and data. Available data sets can be queried by the following keys: ["mmf", "repo_methods", "fnyr", "nypd", "tyld"]
        vintage (str): If the vintage isn’t specified then the whole datasets (preliminary, final, and "as of") will be returned. The valid values for this parameter are: {"p": preliminary, "f": final, "a": as of}
        start_date (str): First date in "YYYY-MM-DD" format for which you want to receive data. If no start_date is given, "1901-01-01" is used.
        end_date (str): Last date in "YYYY-MM-DD" format for which you want to receive data. If no end_date is given, today's date is used.
        periodicity (str): Converts the series to the given periodicity. Available values are: ["A", "AS", "D", "M", "MS", "W", "B", "BM", "BMS", "Q", "BQ", "QS", "BQS", "BA", "BAS"]
        how (str): How to calculate the value for the given periodicity. By default the last value in that period is given. Available values are: ["first", "last", "mean", "median", "sum"]
        remove_nulls (str): If this parameter is set to "true" all nulls in the series will be removed.
        time_format (str): The format for the dates in the series. By default they are returned as strings in the format: YYYY-MM-DD. Available values are: ["date", "ms"]


    Return:
        pd.DataFrame: A tuple of two DataFrames containing the data and metadata for the dataset.
    """
    return __series_dataset(__api, **query)
