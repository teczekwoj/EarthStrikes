import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(
    page_title="Analiza danych uderzeń meteorytów w Ziemię",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)
##############
### SIDEBAR ###
##############
image = Image.open('images/asteroid.png')
st.sidebar.image(image, use_column_width="auto")

####################
### WPROWADZENIE ###
####################
df = pd.read_csv("Meteorite_Landings.csv")
df = df.sort_values(by='year', ascending=True)

#select slider
start_year, end_year = st.select_slider(
    'Wybierz zakres lat',
    options=df["year"],
    value=(1880, 1930))
st.write('Wybrałeś zakres lat:', start_year, 'and', end_year)
#  
filtered_df = df[(df["year"] >= start_year) & (df["year"] <= end_year)]
fig = px.histogram(filtered_df,"year")
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.divider()
st.divider()  
fig = px.histogram(df,"fall")
st.plotly_chart(fig, use_container_width=True)
fig = px.histogram(df,"recclass")
st.plotly_chart(fig, use_container_width=True)

