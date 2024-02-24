import os.path
import zipfile

from tqdm import tqdm

path_source = 'data/source/'
path_target = 'data/unzip/'

zip_filenames = [
    filename for filename in os.listdir(path_source)
    if filename.endswith('.zip')
]
for zip_filename in tqdm(zip_filenames):
    year = int(zip_filename.replace('.zip', ''))
    if os.path.exists(f'{path_target}{year}'):
        continue
    path_to_zip_file = f'{path_source}{zip_filename}'
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        path_target_for_extraction = path_target
        if year > 2019:
            path_target_for_extraction += f'{year}/'
        zip_ref.extractall(path_target_for_extraction)
