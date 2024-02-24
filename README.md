# INMET datasets

This repository has scripts that allow you to generate INMET datasets for public weather stations.

## Datasets

You can find the datasets in `data/`.

### [`metadata.csv`](data/metadata.csv)

Weather station data.

| Column          | Type     | Description                                               | Example             |
|-----------------|----------|-----------------------------------------------------------|---------------------|
| region          | `string` | Region in which the weather station is located.           | `"CO"`              |
| federal_unit    | `string` | Federal unit in which the weather station is located.     | `"DF"`              |
| station         | `string` | Name of the weather station.                              | `"AGUAS EMENDADAS"` |
| code_wmo        | `string` | WMO code of the weather station.                          | `"A045"`            |
| latitude        | `float`  | Latitude of the weather station's geographical position.  | `-15.596491`        |
| longitude       | `float`  | Longitude of the weather station's geographical position. | `-47.625801`        |
| altitude        | `float`  | Altitude of the weather station's geographical position.  | `1030.36`           |
| foundation_date | `date`   | Date the weather station was founded.                     | `2008-10-03`        |

### [`WMO_code.csv`](data/filter_wmo/A304.csv)

Dataset generated after running `transform_filter_wmo.py` (e.g. `A304.csv`).

| Column                             | Type      | Description                                         | Example      |
|------------------------------------|-----------|-----------------------------------------------------|--------------|
| date                               | `date`    | Date of record (`YYYY-MM-DD`).                      | `2003-02-24` |
| time                               | `string`  | Time of record (`HH:mm`), UTC.                      | `"10:00"`    |
| precipitation_total                | `float`   | Total precipitation (mm).                           | `0.0`        |
| atmospheric_pressure_station_level | `float`   | Atmospheric pressure at station level, hourly (mB). | `1009.0`     |
| atmospheric_pressure_max_before    | `float`   | Max. atmospheric pressure at time before (mB).      | `1009.0`     |
| atmospheric_pressure_min_before    | `float`   | Min. atmospheric pressure at time before (mB).      | `1008.5`     |
| global_radiation                   | `float`   | Global radiation (Kj/m²).                           | `1392.0`     |
| temperature_air_dry_bulb           | `float`   | Air temperature - dry bulb, hourly (°C).            | `23.2`       |
| temperature_dew                    | `float`   | Dew point temperature (°C).                         | `22.1`       |
| temperature_max_before             | `float`   | Max. temperature at time before (°C).               | `23.2`       |
| temperature_min_before             | `float`   | Min. temperature at time before (°C).               | `22.9`       |
| temperature_dew_max_before         | `float`   | Max. dew temperature at time before (°C).           | `22.1`       |
| temperature_dew_min_before         | `float`   | Min. dew temperature at time before (°C).           | `21.6`       |
| humidity_relative_max_before       | `float`   | Humidity relative maximum at time before (%).       | `94.0`       |
| humidity_relative_min_before       | `float`   | Humidity relative minimum at time before (%).       | `93.0`       |
| humidity_relative_air              | `float`   | Relative air humidity, hourly (%).                  | `93.0`       |
| wind_direction                     | `float`   | Wind, hourly direction (gr) (° (gr)).               | `318.0`      |
| wind_blast                         | `float`   | Wind, maximum rain (m/s).                           | `3.5`        |
| wind_speed                         | `float`   | Wind, time speed (m/s).                             | `1.5`        |
| wmo_code                           | `string`  | WMO code.                                           | `"A304"`     |

## Scripts

- `extract_zip.py` - Download data from INMET.
- `transform_zip_to_unzip.py` - Unzip the INMET zip files.
- `transform_combine_unzip_by_year.py` - Groups all files from the same year into a single file.
- `transform_filter_wmo.py` - Generates a file with all the records of a weather station.

## Generate

In your environment:

```shell
# Install requirements for scripts
pip install -r requirements.txt

# Run the scripts in this order
python3 extract_zip.py
python3 transform_zip_to_unzip.py
python3 transform_combine_unzip_by_year.py
python3 transform_filter_wmo.py
```

> In `transform_filter_wmo.py`,
  You must change the value of `code_wmo` to the WMO of the desired weather station.

If you have Docker and Makefile installed on your machine,
you can execute the `make build` command to create the image,
followed by `make shell` to access a container and execute
the aforementioned steps to generate the files.

## Contributing

Contributions are more than welcome. Fork, improve and make a pull request.
For bugs, ideas for improvement or other, please create an
[issue](https://github.com/alvarofpp/dataset-inmet/issues).

## License

This project is licensed under the CDLA-Sharing-1.0 License - see the [LICENSE](LICENSE)
file for details.
