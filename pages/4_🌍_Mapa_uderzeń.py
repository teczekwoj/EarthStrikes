import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


############
###CONFIG###
############
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

############
### BODY ###
############
#tabela
st.divider()
file_path = "Meteorite_Landings.csv" 
url= "https://data.nasa.gov/resource/gh4g-9sfh.csv"
try:
    df = pd.read_csv(file_path)
    df = df.dropna(subset=['reclong', 'reclat'])
    st.subheader("Surowe dane")
    st.dataframe(df, 1600, 500)
except FileNotFoundError:
    st.error(f"Plik CSV o nazwie '{file_path}' nie został znaleziony.")

df = df.dropna(subset=['reclong', 'reclat'])

st.map(df,
    latitude='reclat',
    longitude='reclong',
    zoom = 1,
    color='#0044ff',
    size='100')