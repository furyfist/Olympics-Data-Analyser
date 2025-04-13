import numpy as np


def medal_tally(df):
    # This ensures that team events (e.g., hockey) are counted only once per medal, avoiding overcounting caused by listing all team members individually.
    medal_tally = df.drop_duplicates(
        subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])

    medal_tally = medal_tally.groupby('region').sum(
    )[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index()
    # Added a new Column.
    medal_tally['total'] = medal_tally['Gold'] + \
        medal_tally['Silver'] + medal_tally['Bronze']

    medal_tally['Gold'] = medal_tally['Gold'].astype('int')
    medal_tally['Silver'] = medal_tally['Silver'].astype('int')
    medal_tally['Bronze'] = medal_tally['Bronze'].astype('int')
    medal_tally['total'] = medal_tally['total'].astype('int')

    return medal_tally


def country_year_list(df):
    years = sorted(df['Year'].unique().tolist())
    years.insert(0, 'Overall')

    country = np.unique(df['region'].dropna().values.tolist())
    country.sort()
    country = np.insert(country, 0, 'Overall')

    return years, country


def fetch_medal_tally(df, year, country):
    medal_tally = df.drop_duplicates(
        subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = medal_tally
    if year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_tally[medal_tally['region'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df = medal_tally[medal_tally['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df = medal_tally[(medal_tally['Year'] == int(
            year)) & (medal_tally['region'] == country)]

    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values(
            'Year', ascending=True).reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values(
            'Gold', ascending=False).reset_index()

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']

    x['Gold'] = x['Gold'].astype('int')
    x['Silver'] = x['Silver'].astype('int')
    x['total'] = x['total'].astype('int')
    x['Bronze'] = x['Bronze'].astype('int')

    return x


def participating_nations_over_time(df):

    nations_over_time = df.drop_duplicates(['Year', 'region'])[
        'Year'].value_counts().reset_index().sort_values('Year')
    nations_over_time.columns = ['Edition', 'No of Countries']
    return nations_over_time


def events_happening_over_time(df):
    events_over_time = df.drop_duplicates(['Year', 'Event'])[
        'Year'].value_counts().reset_index().sort_values('Year')
    events_over_time.columns = ['Edition', 'No. of Events']
    return events_over_time


def atheletes_over_time(df):
    over_time = df.drop_duplicates(['Year', 'Name'])[
        'Year'].value_counts().reset_index().sort_values('Year')
    over_time.columns = ['Edition', 'No. of Athletes']
    return over_time


def most_successful(df, sport):
    # Remove rows where Medal is NaN
    temp_df = df.dropna(subset=['Medal'])

    # Filter for the given sport if not "Overall"
    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]

    # Get top 10 athletes by medal count
    top_athletes = temp_df['Name'].value_counts().reset_index()
    top_athletes.columns = ['Name', 'Medals']

    # Merge with original df to get more info like Sport
    merged = top_athletes.head(10).merge(df, on='Name', how='left')

    # Drop duplicate athlete names
    result = merged[['Name', 'Medals', 'Sport']].drop_duplicates(subset='Name')

    return result
