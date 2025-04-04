import streamlit as st
import pandas as pd
import Preprocessor

df = Preprocessor.preprocess()

st.sidebar.radio(
    'select an option',
    ('Medal Tally','Overall Analysis', 'Country-Wise Analysis', 'Athlete Wise Analysis')
)

st.dataframe(df)