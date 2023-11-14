import streamlit as st
import pandas as pd
from PIL import Image
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

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
        df = df.dropna(subset=['reclong', 'reclat'])
        return df
    except FileNotFoundError:
        st.error(f"Plik CSV o nazwie '{file_path}' nie został znaleziony.")
        return None

# Load data
df = load_data("Meteorite_Landings.csv")

# Create a folium map with dynamic marker clustering
m = folium.Map(location=[df['reclat'].mean(), df['reclong'].mean()], zoom_start=5)
marker_cluster = MarkerCluster().add_to(m)

# Function to add markers to the marker cluster
def add_markers_to_cluster(df, marker_cluster):
        for index, row in df.iterrows():
            folium.Marker([row['reclat'], row['reclong']]).add_to(marker_cluster)

# Add initial markers to the marker cluster
add_markers_to_cluster(df, marker_cluster)

# Display map using st_folium
st_data = st_folium(m)