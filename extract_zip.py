from datetime import datetime
import os.path
import requests
from tqdm import tqdm

path = 'data/source/'

first_year = 2000
current_year = datetime.now().year
years = range(first_year, current_year)
url = 'https://portal.inmet.gov.br/uploads/dadoshistoricos/{year}.zip'

for year in tqdm(range(first_year, current_year+1)):
    url_file = url.format(year=year)
    filename = f'{path}{year}.zip'
    if os.path.exists(filename):
        continue

    with requests.get(url_file) as file_response:
        with open(filename, 'wb') as file_to_save:
            file_to_save.write(file_response.content)
