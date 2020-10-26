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
data_extractor = DataExtractor()
metadata_extractor = MetadataExtractor()
year_start = 2019

for dirname in list_dirs:
    if int(dirname) < year_start:
        continue
    files_by_dir = [filename for filename in list_files if dirname in filename]

    progress_bar = tqdm(files_by_dir)
    for filename in progress_bar:
        progress_bar.set_description("({}) Processing {}".format(dirname, filename))
        metadata = metadata_extractor.extract(filename)
        data_extractor.extract(filename, metadata)

    data_df = pd.concat(data_extractor.data)
    data_df.to_csv('data/per_year/{}.csv'.format(dirname), sep=',', encoding='utf-8', index=False)
    data_extractor.data = []

metadata_df = pd.DataFrame.from_dict(metadata_extractor.data)
metadata_df.sort_values(['foundation_date'])\
    .drop_duplicates(subset=['code_wmo'], keep='last')\
    .sort_values(['region', 'federal_unit', 'station'])\
    .to_csv('data/metadata.csv', sep=',', encoding='utf-8', index=False)
