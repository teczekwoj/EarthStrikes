import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

st.set_page_config(
    page_title="Analiza danych uderzeń meteorytów w Ziemię",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

####################
### WPROWADZENIE ###
####################
t1 = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.   
Lorem ipsum Sit sunt duis excepteur ut excepteur ex do nostrud aute qui.
'''
st.title("Analiza danych uderzeń meteorytów w Ziemię 🚀")
st.markdown("Ullamco occaecat cillum ullamco minim. Id ad fugiat qui nostrud nulla fugiat aute mollit.  Nulla do tempor aliquip ex cillum magna est fugiat ex. Excepteur incididunt nisi proident deserunt commodo mollit est minim. Irure ex in mollit aliqua sit commodo excepteur laboris ut excepteur consequat consectetur sint.", help="Lorem ipsum coś tam")
st.write("Elit laborum anim occaecat eu irure ea non aliquip reprehenderit. Nostrud laborum sunt aute incididunt adipisicing velit commodo est incididunt fugiat ullamco. Dolor sint qui consequat laboris officia duis reprehenderit irure cupidatat amet aliquip nostrud dolor. Labore consequat dolor nulla nisi id ut ea culpa fugiat. Dolor commodo labore esse tempor in amet anim.")
st.write(t1)




##############
### SIDEBAR ###
##############
st.sidebar.markdown("Tu kiedyś coś będzie")

############
### BODY ###
############

# Wczytywanie pliku CSV z folderu "Projekt_v1"
file_path = "Meteorite_Landings.csv" 
# Sprawdź, czy plik istnieje
try:
    df = pd.read_csv(file_path)
    st.subheader("Surowe dane")
    st.write(df)
except FileNotFoundError:
    st.error(f"Plik CSV o nazwie '{file_path}' nie został znaleziony.")

# Statystyki podstawowe dotyczące mas meteorytów
st.subheader("Statystyki dotyczące mas meteorytów")
mass_stats = df['mass (g)'].describe()
st.write(mass_stats)


