import pandas as pd

# Load datasets
df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

def preprocess():
    global df, region_df

    # Filter only Summer Olympics data
    df = df[df['Season'] == 'Summer']

    # Step 1: Safely drop conflicting columns from df
    columns_to_drop = ['region', 'notes']
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

    # Step 2: Merge with region data
    df = df.merge(region_df, on='NOC', how='left')

    # Drop exact duplicate rows
    df.drop_duplicates(inplace=True)

    # One-hot encode 'Medal' column and add to original df
    df = pd.concat([df, pd.get_dummies(df['Medal']).astype(int)], axis=1)

    return df
