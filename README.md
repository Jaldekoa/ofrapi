# ofrapi Documentation
This repository contains a Python wrapper to easily retrieve data from the Office of Financial Research (OFR) in Pandas format using the official API.

- **[Short-term Funding Monitor: ofrapi.stfm](ofrapi/stfm/README.md)**
- **[Hedge Fund Monitor: ofrapi.hfm](ofrapi/hfm/README.md)**

## Short-term Funding Monitor
The Short-term Funding Monitor (STFM) application programming interface (API) allows a remote application to query the Office of Financial Research for data without the need for a human intermediary to download data manually. While some API calls might be used every day, others are intended for use when setting up a remote application for a periodic refresh.

We have provided this open interface for public use. This API does not require tokens or registration, so feel free to use it immediately.

### Get Series Information (ofrapi.stfm.get_series_info)
The following retrieve the metadata attached to each specified series.

| Method                   | Description                                                                             |
|--------------------------|-----------------------------------------------------------------------------------------|
| ```metadata_mnemonics``` | Retrieves all series as unique identifiers referred to as mnemonics.                    |
| ```metadata_query```     | Retrieves the information for a specified series.                                       |
| ```metadata_search```    | Retrieves a list of series with identifying information that matches a query condition. |

### Get Series Data (ofrapi.stfm.get_series_data)
The following retrieve the data for specified series.

| Method                  | Description                                                                  |
|-------------------------|------------------------------------------------------------------------------|
| ```series_timeseries``` | Retrieves the data for a single series.                                      |
| ```calc_spread```       | Retrieves the spread between two series as a list of data points and values. |

### Get Series Information & Data (ofrapi.stfm.series_info_data)
The following retrieve the metadata and data for specified series.

| Method                 | Description                                                                |
|------------------------|----------------------------------------------------------------------------|
| ```series_full```      | Retrieves the information and data for a single series.                    |
| ```series_multifull``` | Retrieves the information and data for a group of series.                  |
| ```series_dataset```   | Retrieves the information and data for all series in a specified data set. |


## Hedge Fund Monitor
The Hedge Fund Monitor (HFM) application programming interface (API) allows a remote application to query the Office of Financial Research for data without the need for a human intermediary to download data manually. While some API calls might be used every day, others are intended for use when setting up a remote application for a periodic refresh.

We have provided this open interface for public use. This API does not require tokens or registration, so feel free to use it immediately.

### Get Series Information (ofrapi.hfm.get_series_info)
The following retrieve the metadata attached to each specified series.

| Method                   | Description                                                                             |
|--------------------------|-----------------------------------------------------------------------------------------|
| ```metadata_mnemonics``` | Retrieves all series as unique identifiers referred to as mnemonics.                    |
| ```metadata_query```     | Retrieves the information for a specified series.                                       |
| ```metadata_search```    | Retrieves a list of series with identifying information that matches a query condition. |

### Get Series Data (ofrapi.hfm.get_series_data)
The following retrieve the data for specified series.

| Method                  | Description                                                                  |
|-------------------------|------------------------------------------------------------------------------|
| ```series_timeseries``` | Retrieves the data for a single series.                                      |
| ```calc_spread```       | Retrieves the spread between two series as a list of data points and values. |

### Get Series Information & Data (ofrapi.hfm.series_info_data)
The following retrieve the metadata and data for specified series.

| Method                 | Description                                                                |
|------------------------|----------------------------------------------------------------------------|
| ```series_full```      | Retrieves the information and data for a single series.                    |
| ```series_multifull``` | Retrieves the information and data for a group of series.                  |
| ```series_dataset```   | Retrieves the information and data for all series in a specified data set. |
| ```categories```       | Returns a csv file containing the data for a category.                     |


## API Documentation
- [Short-term Funding Monitor - API (OFR)](https://www.financialresearch.gov/short-term-funding-monitor/api/).
- [Hedge Fund Monitor - API (OFR)](https://www.financialresearch.gov/hedge-fund-monitor/api/).
