import streamlit as st
import pandas as pd
import Preprocessor
import helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import scipy


# Load datasets
df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = Preprocessor.preprocess(df, region_df)

st.sidebar.title("Olympics Analysis")
user_menu = st.sidebar.radio(
    'Select an option',
    ('Medal Tally', 'Overall Analysis',
     'Country-Wise Analysis', 'Athlete Wise Analysis')

)

# st.dataframe(df)

if user_menu == "Medal Tally":
    st.sidebar.header("Medal Tally")
    years, country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select the Year", years)
    selected_country = st.sidebar.selectbox("Select the country", country)

    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)

    if selected_country == "Overall" and selected_year == "Overall":
        st.title("Overall Performance Across All Years and Countries")
    elif selected_country == "Overall" and selected_year != "Overall":
        st.title(f"Performance Across All Countries in {selected_year}")
    elif selected_country != "Overall" and selected_year == "Overall":
        st.title(f"Performance of {selected_country} Across All Years")
    else:
        st.title(f"Performance of {selected_country} in {selected_year}")

    st.table(medal_tally)

if user_menu == "Overall Analysis":
    st.sidebar.header("Overall Analysis")

    editions = df['Year'].unique().shape[0]
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nation = df['region'].unique().shape[0]

    st.title("Top Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.title("Editions")
        st.header(editions)
    with col2:
        st.title("Hosts")
        st.header(cities)
    with col3:
        st.title("Sports")
        st.header(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.title("Events")
        st.header(events)
    with col2:
        st.title("Athletes")
        st.header(athletes)
    with col3:
        st.title("Nations")
        st.header(nation)

    st.title('# Participating Nations Over The Years')
    nations_over_time = helper.participating_nations_over_time(df)
    fig = px.line(nations_over_time, x="Edition", y="No of Countries")
    st.plotly_chart(fig)

    st.title('# Number of Events Over the Years')
    events_over_time = helper.events_happening_over_time(df)
    fig = px.line(events_over_time, x='Edition', y='No. of Events')
    st.plotly_chart(fig)

    st.title('# Number of Athletes Over the Years')
    over_time = helper.atheletes_over_time(df)
    fig = px.line(over_time, x='Edition', y='No. of Athletes')
    st.plotly_chart(fig)

    st.title("No. of Events over time(Every Sport)")
    fig, ax = plt.subplots(figsize=(20, 20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year',
                    values='Event', aggfunc='count').fillna(0).astype('int'), annot=True)
    st.pyplot(fig)

    st.title("Most successful Athletes")
    sport_list = sorted(df['Sport'].drop_duplicates().tolist())
    sport_list.insert(0, 'Overall')

    selected_sport = st.selectbox('Select a Sport', sport_list)
    x = helper.most_successful(df, selected_sport)
    st.table(x)

if user_menu == 'Country-Wise Analysis':

    st.sidebar.title('Country-Wise Analysis')
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox('Select a Country',country_list)

    country_df = helper.yearwise_medal_tally(df,selected_country)
    fig = px.line(country_df, x="Year", y="Medal")
    st.title(selected_country + " Medal Tally over the years")
    st.plotly_chart(fig)

    st.title(selected_country + " excels in the following sports")
    pt = helper.country_event_heatmap(df,selected_country)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt,annot=True)
    st.pyplot(fig)

    st.title("Top 10 athletes of " + selected_country)
    top10_df = helper.most_successful_countrywise(df,selected_country)
    st.table(top10_df)

if user_menu == 'Athlete Wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Height Vs Weight')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = helper.weight_v_height(df, selected_sport)

    fig, ax = plt.subplots()
    ax = sns.scatterplot(
        x=temp_df['Weight'], 
        y=temp_df['Height'], 
        hue=temp_df['Medal'], 
        style=temp_df['Sex'], 
        s=60
    )
    st.pyplot(fig)

    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)
