import os

import pandas as pd
from tqdm import tqdm

from extracts import DataExtractor, MetadataExtractor

list_dirs = []
list_files = []
for (dirpath, dirnames, filenames) in os.walk('data/unzip'):
    list_dirs += dirnames
    list_files += [os.path.join(dirpath, file) for file in filenames]

list_dirs.sort()
list_files.sort()

metadata_extractor = MetadataExtractor()
data_extractor = DataExtractor()
year_start = 2000

for dirname in list_dirs:
    if int(dirname) < year_start:
        continue
    file_target = f'data/per_year/{dirname}.csv'
    if os.path.exists(file_target):
        continue
    files_by_dir = [filename for filename in list_files if dirname in filename]
    progress_bar = tqdm(files_by_dir)
    for filename in progress_bar:
        progress_bar.set_description(f'({dirname}) Processing {filename}')
        metadata = metadata_extractor.extract(filename)
        data_extractor.extract(filename, metadata)

    data_df = pd.concat(data_extractor.data)
    data_df.to_csv(
        f'data/per_year/{dirname}.csv',
        sep=',',
        encoding='utf-8',
        index=False
    )
    del data_df
    data_extractor.clear()

metadata_file = 'data/metadata.csv'
if not os.path.exists(metadata_file):
    metadata_df = pd.DataFrame.from_dict(metadata_extractor.data)
    metadata_df.sort_values(['foundation_date'])\
        .drop_duplicates(subset=['code_wmo'], keep='last')\
        .sort_values(['region', 'federal_unit', 'station'])\
        .to_csv(metadata_file, sep=',', encoding='utf-8', index=False)
