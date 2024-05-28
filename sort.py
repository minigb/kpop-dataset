import pandas as pd
from pathlib import Path

# Load the dataset
fn = Path('kpop-dataset/song_list.csv')
data = pd.read_csv(fn)

# sort by Label, Artist, and Year
data = data.sort_values(by=['Label', 'Artist', 'Year'])
# sorted_fn = Path('kpop-dataset/sorted_song_list.csv')
sorted_fn = fn
data.to_csv(sorted_fn, index=False)