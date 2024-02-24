import os

import pandas as pd
from tqdm import tqdm

main_dir = 'data/per_year/'
wmo_code = 'A304'  # Natal-RN

list_files = []
for (dirpath, dirnames, filenames) in os.walk(main_dir): # noqa: B007
    list_files += [
        os.path.join(dirpath, filename) for filename in filenames
        if filename.endswith('.csv')
    ]
dfs = []

list_files.sort()

progress_bar = tqdm(list_files)
for filename in progress_bar:
    progress_bar.set_description('Processing {filename}')
    df_now = pd.read_csv(filename)
    dfs.append(df_now[df_now['wmo_code'] == wmo_code])
    del(df_now)

large_df = pd.concat(dfs, axis=0, ignore_index=True)
large_df.to_csv(f'data/filter_wmo/{wmo_code}.csv', index=False)
