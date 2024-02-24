import gc
import pandas as pd
from extracts.clean_functions import (
    clean_date,
    clean_time,
    clean_numeric,
)


class DataExtractor:
    def __init__(self):
        self.data = []
        self.columns = {
            'Data': 'date',
            'DATA (YYYY-MM-DD)': 'date',
            'Hora UTC': 'time',
            'HORA (UTC)': 'time',
            'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)': 'precipitation_total',
            'PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)': 'atmospheric_pressure_station_level',
            'PRESSÃO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)': 'atmospheric_pressure_max_before',
            'PRESSÃO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB)': 'atmospheric_pressure_min_before',
            'RADIACAO GLOBAL (Kj/m²)': 'global_radiation',
            'RADIACAO GLOBAL (KJ/m²)': 'global_radiation',
            'TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)': 'temperature_air_dry_bulb',
            'TEMPERATURA DO PONTO DE ORVALHO (°C)': 'temperature_dew',
            'TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)': 'temperature_max_before',
            'TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)': 'temperature_min_before',
            'TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (°C)': 'temperature_dew_max_before',
            'TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (°C)': 'temperature_dew_min_before',
            'UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)': 'humidity_relative_max_before',
            'UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)': 'humidity_relative_min_before',
            'UMIDADE RELATIVA DO AR, HORARIA (%)': 'humidity_relative_air',
            'VENTO, DIREÇÃO HORARIA (gr) (° (gr))': 'wind_direction',
            'VENTO, RAJADA MAXIMA (m/s)': 'wind_blast',
            'VENTO, VELOCIDADE HORARIA (m/s)': 'wind_speed',
        }

    def clear(self) -> None:
        del self.data
        gc.collect()
        self.data = []

    def extract(self, filename: str, metadata: dict) -> bool:
        data = pd.read_csv(filename, sep=';', skiprows=8, encoding='ISO-8859-1')
        data = data.rename(columns=self.columns)
        data.drop(data.columns[len(data.columns) - 1], axis=1, inplace=True)
        data['code_wmo'] = metadata['code_wmo']
        data['date'] = data['date'].map(clean_date)
        data['time'] = data['time'].map(clean_time)
        numeric_cols = [
            'precipitation_total',
            'atmospheric_pressure_station_level',
            'atmospheric_pressure_max_before',
            'atmospheric_pressure_min_before',
            'global_radiation',
            'temperature_air_dry_bulb',
            'temperature_dew',
            'temperature_max_before',
            'temperature_min_before',
            'temperature_dew_max_before',
            'temperature_dew_min_before',
            'humidity_relative_max_before',
            'humidity_relative_min_before',
            'humidity_relative_air',
            'wind_direction',
            'wind_blast',
            'wind_speed',
        ]
        for numeric_col in numeric_cols:
            data[numeric_col] = data[numeric_col].map(clean_numeric)

        self.data.append(data.copy())
        del data

        return True
