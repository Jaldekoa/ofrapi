from urllib.parse import urlencode
from functools import reduce
import pandas as pd
import requests

__all__ = ['hfm', 'stfm']
__base_url = "https://data.financialresearch.gov"


def __encode_url(api: str, endpoint: str, query: dict) -> str:
    if query is None:
        print(f"{__base_url}/{api}/{endpoint}")
        return f"{__base_url}/{api}/{endpoint}"
    else:
        print(f"{__base_url}/{api}/{endpoint}?{urlencode(query)}")
        return f"{__base_url}/{api}/{endpoint}?{urlencode(query)}"


def __get_data_from_url(api: str, endpoint: str, query: dict) -> dict:
    url = __encode_url(api, endpoint, query)
    res = requests.get(url).json()
    return res


def __metadata_mnemonics(api: str, **query):
    raw_json = __get_data_from_url(api, "metadata/mnemonics", query)

    if query.get("dataset", False):
        return pd.DataFrame(raw_json)
    elif query.get("output", False):
        dfs = [pd.json_normalize(raw_json, k).assign(dataset=k) for k, v in raw_json.items()]
        return pd.concat(dfs, ignore_index=True)
    else:
        return pd.DataFrame(raw_json)


def __metadata_query(api: str, mnemonic: str, **query):
    raw_json = __get_data_from_url(api, "metadata/query", {"mnemonic": mnemonic, **query})
    return pd.json_normalize(raw_json, max_level=1)


def __metadata_search(api: str, query: str):
    raw_json = __get_data_from_url(api, "metadata/search", {"query": query})
    return pd.DataFrame(raw_json)


def __series_timeseries(api: str, mnemonic, **query) -> pd.DataFrame:
    raw_json = __get_data_from_url(api, "series/timeseries", {"mnemonic": mnemonic, **query})
    df_data = pd.DataFrame(raw_json, columns=["date", "value"])
    df_data["date"], df_data["value"] = pd.to_datetime(df_data["date"]), pd.to_numeric(df_data["value"],
                                                                                       errors="coerce")
    return df_data


def __calc_spread(api: str, x: str, y: str, **query) -> pd.DataFrame:
    raw_json = __get_data_from_url(api, "calc/spread", {"x": x, "y": y, **query})
    df_data = pd.DataFrame(raw_json, columns=["date", "value"])
    df_data["date"], df_data["value"] = pd.to_datetime(df_data["date"]), pd.to_numeric(df_data["value"],
                                                                                       errors="coerce")
    return df_data


def __series_full(api: str, mnemonic: str, **query) -> (pd.DataFrame, pd.DataFrame):
    df_timeseries = __series_timeseries(api, mnemonic, **query)
    df_metadata = __metadata_query(api, mnemonic, **query)
    return df_timeseries, df_metadata


def __series_multifull(api: str, mnemonics: str, **query) -> (pd.DataFrame, pd.DataFrame):
    dfs = [__series_full(api, mnemonic, **query) for mnemonic in mnemonics.split(",")]
    timeseries, metadata = [el_one for el_one, el_two in dfs], [el_two for el_one, el_two in dfs]
    return pd.concat(timeseries, ignore_index=True), pd.concat(metadata, ignore_index=True)


def __series_dataset(api: str, **query) -> (pd.DataFrame, pd.DataFrame):
    raw_json = __get_data_from_url(api, "series/dataset", query)

    if query:

        dfs = [pd.DataFrame(data["timeseries"]["aggregation"], columns=["date", name]) for name, data in raw_json["timeseries"].items()]
        return reduce(lambda left_df, right_df: pd.merge(left_df, right_df, on="date", how="outer"), dfs)

    else:
        return pd.DataFrame([(key, value.get("long_name"), value.get("short_name")) for key, value in raw_json.items()],
                            columns=["database", "long_name", "short_name"])


def __categories(api: str, category: str) -> pd.DataFrame:
    df_data = pd.read_csv(__encode_url(api, "categories", {"category": category}))
    df_data["date"] = pd.to_datetime(df_data["date"])
    return df_data
