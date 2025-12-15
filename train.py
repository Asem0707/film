import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib


ratings = pd.read_csv('ratings.csv') # columns: user_id,movie_id,rating
pivot = ratings.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)
movie_ids = pivot.columns.tolist()
item_matrix = pivot.values.T
item_sim = cosine_similarity(item_matrix)
np.save('artifacts/item_sim.npy', item_sim)
joblib.dump({mid:i for i,mid in enumerate(movie_ids)}, 'artifacts/movie_id_index.pkl')