import csv


class Metadata:
    def __init__(self):
        self.data = {
            'regiao': [],
            'uf': [],
            'estacao': [],
            'codigo_wmo': [],
            'latitude': [],
            'longitude': [],
            'altitude': [],
            'data_fundacao': [],
        }
    
    def extract(self, filename: str) -> bool:
        with open(filename, newline='', encoding='ISO-8859-1') as f:
            reader = csv.reader(f, delimiter=';')
            
            self.data['regiao'].append(self._extract_value_from_csv_row(next(reader)))
            self.data['uf'].append(self._extract_value_from_csv_row(next(reader)))
            self.data['estacao'].append(self._extract_value_from_csv_row(next(reader)))
            self.data['codigo_wmo'].append(self._extract_value_from_csv_row(next(reader)))
            self.data['latitude'].append(self._extract_value_from_csv_row(next(reader)))
            self.data['longitude'].append(self._extract_value_from_csv_row(next(reader)))
            self.data['altitude'].append(self._extract_value_from_csv_row(next(reader)))

            data_fundacao = self._extract_value_from_csv_row(next(reader))
            if '/' in data_fundacao:
                data_fundacao = data_fundacao.split('/')
                data_fundacao.reverse()
                data_fundacao = '20' + '-'.join(data_fundacao)

            self.data['data_fundacao'].append(data_fundacao)
    
            f.close()
    
        return True
    
    def _extract_value_from_csv_row(self, row) -> str:
        return row[1].replace(',', '.')
