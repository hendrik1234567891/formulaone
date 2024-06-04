import json
import os

import requests
import pandas as pd
import numpy as np

from core import get_raw_data
from helpers import get_raw_data_path

def load_race(year=2013):
    movies=get_raw_data(year)

    # Normalize JSON
    movies_df = pd.json_normalize(movies['Items'])

    # Encoding the Genre Columns with Hot-Encoding
    genres = pd.unique(pd.Series(np.concatenate(movies_df['info.genres'])))
    movies_df[[list(genres)]] = np.NaN

    for (col, data) in movies_df.loc[:, list(genres)].items():
        movies_df[col] = [1 if col in x else 0 for x in movies_df['info.genres']]

    raw_data_path = get_raw_data_path()

    raw_data_path.mkdir(parents=True, exist_ok=True)

    movies_df.to_csv(os.path.join(raw_data_path,"form1data"))
    return movies_df








