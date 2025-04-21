import pandas as pd
import numpy as ny
from sklearn.impute import SimpleImputer


df = pd.read_csv(r'D:\Elevate Lab Internship\Netflix Movies and TV Shows\netflix_titles.csv')

# print("Dataset preview:\n", df.head())

# print(f"\nShape of dataset: {df.shape}")

# print("\nColumn Data Types:\n", df.dtypes)

# print("\nMissing Values in Each Column:\n", df.isnull().sum())

df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df.dropna(subset=['date_added'], inplace=True)

df['rating'] = df['rating'].fillna(df['rating'].mode()[0])
# df['duration'] = df['duration'].fillna(df['duration'].mode()[0])

# For movies
movie_mode = df[df['type'] == 'Movie']['duration'].mode()[0]
df.loc[(df['type'] == 'Movie') & (df['duration'].isnull()), 'duration'] = movie_mode

# For TV shows
tv_mode = df[df['type'] == 'TV Show']['duration'].mode()[0]
df.loc[(df['type'] == 'TV Show') & (df['duration'].isnull()), 'duration'] = tv_mode


print("\nMissing Values After Cleaning:\n", df.isnull().sum())

df.drop_duplicates(inplace=True)

# Standardize 'country' column: lowercase, strip spaces, unify common names
df['country'] = df['country'].str.lower().str.strip()
df['country'] = df['country'].replace({
    'usa': 'united states',
    'us': 'united states',
    'united states of america': 'united states',
    'uk': 'united kingdom'
})

# Standardize 'type' column: lowercase, strip spaces
df['type'] = df['type'].str.lower().str.strip()

# Standardize 'rating' column: lowercase, strip spaces
df['rating'] = df['rating'].str.lower().str.strip()

# Standardize 'listed_in' (genres): lowercase, strip spaces
df['listed_in'] = df['listed_in'].str.lower().str.strip()

# (Optional) Standardize other relevant text columns similarly
# For example, if you want to standardize director names:
df['director'] = df['director'].str.lower().str.strip()

df.to_csv('netflix_titles_standardized.csv', index=False)

# Convert to dd-mm-yyyy format
df['date_added'] = df['date_added'].dt.strftime('%d-%m-%Y')

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

print(df.dtypes)

df['release_year'] = df['release_year'].astype(int)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
movie_mask = df['type'].str.lower() == 'movie'
tv_mask = df['type'].str.lower() == 'tv show'
df.loc[movie_mask, 'duration'] = df.loc[movie_mask, 'duration'].str.replace(' min', '').astype(float)
df.loc[tv_mask, 'duration'] = df.loc[tv_mask, 'duration'].str.replace(' Seasons', '').str.replace(' Season', '').astype(float)
df['duration'] = df['duration'].astype(float)

print(df.dtypes)
