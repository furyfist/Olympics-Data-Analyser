import streamlit as st
import pandas as pd

st.sidebar.radio(
    'select an option'
    ('Medal Tally','Overall Analysis', 'Country-Wise Analysis', 'Athlete Wise Analysis')
)