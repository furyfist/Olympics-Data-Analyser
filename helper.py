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
    years = sorted(df['Year'].unique().tolist())
    years.insert(0,'Overall')

    country = np.unique(df['region'].dropna().values.tolist())
    country.sort()
    country = np.insert(country,0,'Overall')

    return years,country

def fetch_medal_tally(df, year, country):
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall': 
        temp_df = medal_tally
    if year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_tally[medal_tally['region'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df = medal_tally[medal_tally['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df = medal_tally[(medal_tally['Year'] == int(year)) & (medal_tally['region'] == country)]

    if flag == 1: 
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year', ascending=True).reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index()

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']

    x['Gold'] = x['Gold'].astype('int')
    x['Silver'] = x['Silver'].astype('int')
    x['total'] = x['total'].astype('int')
    x['Bronze'] = x['Bronze'].astype('int')

    return x