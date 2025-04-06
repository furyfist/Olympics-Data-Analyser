import streamlit as st
import pandas as pd
import Preprocessor,helper

# Load datasets
df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = Preprocessor.preprocess(df,region_df)

st.sidebar.title("Olympics Analysis")
user_menu = st.sidebar.radio(
    'Select an option',
    ('Medal Tally','Overall Analysis', 'Country-Wise Analysis', 'Athlete Wise Analysis')

)

st.dataframe(df)

if user_menu == "Medal Tally":
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select the Year",years)
    selected_country = st.sidebar.selectbox("Select the country",country)

    medal_tally = helper.medal_tally(df)
    st.dataframe(medal_tally)