# Task_1
Task 1: Data Cleaning and Preprocessing

## Overview
This project demonstrates data cleaning and preprocessing on the Netflix Movies and TV Shows dataset.

## How to Run
1. Clone the repository.
2. Install dependencies (`pip install pandas numpy scikit-learn`).
3. Run the cleaning script: `python clean_netflix_data.py`.

## Data Source
- Netflix Movies and TV Shows Dataset (original CSV file used for cleaning).

## Files
- `clean_netflix_data.py`: Python script containing the data cleaning code.
- `netflix_titles.csv`: Raw dataset.
- `netflix_titles_standardized.csv`: Cleaned and standardized output dataset.

## Cleaning Steps
- Handled missing values in columns like `director`, `cast`, `country`, `rating`, and `duration`.
- Converted `date_added` to datetime and formatted it to `dd-mm-yyyy`.
- Removed duplicate rows to ensure data integrity.
- Standardized text columns (`country`, `type`, `rating`, `listed_in`, `director`) by converting to lowercase and stripping spaces.
- Unified common country names (e.g., 'usa' to 'united states').
- Cleaned and converted `duration` column to numeric values separately for movies and TV shows.
- Renamed column headers to lowercase and replaced spaces with underscores for consistency.

## Results
- Dataset cleaned with no missing values except for a few handled appropriately.
- Data types corrected for analysis readiness.
- Cleaned dataset saved as `netflix_titles_standardized.csv`.

## Acknowledgments
- Netflix for providing the dataset.

## License
MIT
