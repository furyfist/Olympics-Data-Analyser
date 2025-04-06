import numpy as np

def medal_tally(df):
    # This ensures that team events (e.g., hockey) are counted only once per medal, avoiding overcounting caused by listing all team members individually.
    medal_tally = df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])

    medal_tally = medal_tally.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
    # Added a new Column.
    medal_tally['total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']

    medal_tally['Gold'] = medal_tally['Gold'].astype('int')
    medal_tally['Silver'] = medal_tally['Silver'].astype('int')
    medal_tally['Bronze'] = medal_tally['Bronze'].astype('int')
    medal_tally['total'] = medal_tally['total'].astype('int')
    
    return medal_tally

def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort
    years.insert(0,'Overall')

    country = np.unique(df['region'].dropna().values.tolist())
    country.sort()
    country = np.insert(country,0,'Overall')

    return years,country

