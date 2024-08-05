from ofrapi import __metadata_mnemonics, __metadata_query, __metadata_search
from ofrapi.stfm import __api

__all__ = ["metadata_mnemonics", "metadata_query", "metadata_search"]


def metadata_mnemonics(**query):
    """
    Returns all series available through the API. If no parameters are specified, then this route returns a list of
    all mnemonics. Using a parameter returns a list of hashes that contain the mnemonic along with the series name.

    Keyword Args:
        dataset (str): The data set for which you want to retrieve mnemonics. Available data sets can be queried by the following keys: ["mmf", "repo_methods", "fnyr", "nypd", "tyld"]
        output (str): The only allowable output value is "by_dataset" which will return a hash with the top-level keys being the data sets and their value being a list of mnemonics.

    Return:
        pd.DataFrame: A DataFrame containing the metadata mnemonics data.
    """
    return __metadata_mnemonics(__api, **query)


def metadata_query(mnemonic: str, **query):
    """
    Returns specific metadata for the given mnemonic. Series metadata is organized into fields; some fields have
    subfields. If you do not specify the fields parameter, all the metadata for that mnemonic is returned. The
    metadata is returned as a single hash with the field names and their value.

    Args:
        mnemonic (str): **This parameter is required**. The mnemonic for which you want to retrieve metadata.

    Return:
        pd.DataFrame: A DataFrame containing the metadata query data.
    """
    return __metadata_query(__api, mnemonic, **query)


def metadata_search(query: str):
    """
    Returns a list of data sets and series that contain field values that match the given search query. The results are returned with the following fields:

    - mnemonic: unique identifier for the series
    - dataset: identifier for the data set that the series is a part of
    - field: the metadata field that satisfies the search query
    - value: the value of the field that satisfies the search query
    - type: format of the data within the field
    If the metadata is at the data set level, then "mnemonic" will be "none".

    Args:
        query (str): **This parameter is required**. The value for which you want to search. * and ? are supported.

    Returns:
        pd.DataFrame: A DataFrame containing the metadata search by query data.
    """
    return __metadata_search(__api, query)
