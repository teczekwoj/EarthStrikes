import streamlit as st
import pandas as pd
from PIL import Image
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim

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

# Function to load data with caching
@st.cache_data
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        df = df[['reclong', 'reclat']]
        df = df.dropna(subset=['reclong', 'reclat'])
        df = df.rename(columns={'reclong': 'lon', 'reclat': 'lat'})
        return df
    except FileNotFoundError:
        st.error(f"Plik CSV o nazwie '{file_path}' nie został znaleziony.")
        return None

# Load data
df = load_data("Meteorite_Landings.csv")

st.dataframe(df, 1600, 500)

st.map(df)

