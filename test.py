import streamlit as st
import pandas as pd
import altair as alt

trafficking_df = pd.read_csv('Trafficking_Data.csv')

st.dataframe(trafficking_df)

bar = alt.Chart(trafficking_df).mark_bar().encode(
    alt.X('gender', title= 'gender'),
    alt.Y('count(gender)', title= 'count')
)

st.altair_chart(bar, use_container_width= True)