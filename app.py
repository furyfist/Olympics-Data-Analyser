import streamlit as st
import pandas as pd
import Preprocessor,helper

# Load datasets
df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = Preprocessor.preprocess(df,region_df)

user_menu = st.sidebar.radio(
    'select an option',
    ('Medal Tally','Overall Analysis', 'Country-Wise Analysis', 'Athlete Wise Analysis')
)

st.dataframe(df)

if user_menu == "Medal Tally":
    medal_tally = helper.medal_tally(df)
    st.dataframe(medal_tally)