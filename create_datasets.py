import os
import pandas as pd
from tqdm import tqdm
from extracts.Metadata import Metadata


list_files = []
for (dirpath, dirnames, filenames) in os.walk('data/unzip'):
    list_files += [os.path.join(dirpath, file) for file in filenames]
list_files.sort()

metadata = Metadata()
progress_bar = tqdm(list_files)
for filename in progress_bar:
    progress_bar.set_description("Processing %s" % filename)
    metadata.extract(filename)

metadata_df = pd.DataFrame.from_dict(metadata.data)
metadata_df.sort_values(['data_fundacao'])\
    .drop_duplicates(subset=['codigo_wmo'], keep='last')\
    .sort_values(['regiao', 'uf', 'estacao'])\
    .to_csv('data/metadata.csv', sep=',', encoding='utf-8', index=False)
