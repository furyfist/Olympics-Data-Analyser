import streamlit as st
import pandas as pd
import Preprocessor
import helper

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
