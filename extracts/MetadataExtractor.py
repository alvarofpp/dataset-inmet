import csv


class MetadataExtractor:
    def __init__(self):
        self.data = {
            'region': [],
            'federal_unit': [],
            'station': [],
            'code_wmo': [],
            'latitude': [],
            'longitude': [],
            'altitude': [],
            'foundation_date': [],
        }
    
    def extract(self, filename: str) -> dict:
        with open(filename, newline='', encoding='ISO-8859-1') as f:
            reader = csv.reader(f, delimiter=';')
            
            self.data['region'].append(self._extract_value_from_csv_row(next(reader)))
            self.data['federal_unit'].append(self._extract_value_from_csv_row(next(reader)))
            self.data['station'].append(self._extract_value_from_csv_row(next(reader)))
            self.data['code_wmo'].append(self._extract_value_from_csv_row(next(reader)))
            self.data['latitude'].append(self._extract_value_from_csv_row(next(reader)))
            self.data['longitude'].append(self._extract_value_from_csv_row(next(reader)))
            self.data['altitude'].append(self._extract_value_from_csv_row(next(reader)))

            data_fundacao = self._extract_value_from_csv_row(next(reader))
            if '/' in data_fundacao:
                data_fundacao = data_fundacao.split('/')
                data_fundacao.reverse()
                data_fundacao = '20' + '-'.join(data_fundacao)

            self.data['foundation_date'].append(data_fundacao)
    
            f.close()
    
        return {
            'region': self.data['region'][-1],
            'federal_unit': self.data['federal_unit'][-1],
            'station': self.data['station'][-1],
            'code_wmo': self.data['code_wmo'][-1],
            'latitude': self.data['latitude'][-1],
            'longitude': self.data['longitude'][-1],
            'altitude': self.data['altitude'][-1],
            'foundation_date': self.data['foundation_date'][-1],
        }
    
    def _extract_value_from_csv_row(self, row) -> str:
        return row[1].replace(',', '.')
