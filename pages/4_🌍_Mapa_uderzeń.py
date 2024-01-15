import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

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


df = pd.read_csv("Meteorite_Landings.csv")
df_countries = pd.read_csv("Meteorite_Landings_Countries.csv")
col1, col2 = st.columns([0.7, 0.3])
with col1:  
# Mapa poglądowa
    fig = px.scatter_mapbox(
        df,
        lat="reclat", 
        lon="reclong",
        hover_name="name",
        zoom=0.7,
        center=dict(lon=0, lat=0),
        color_discrete_sequence=['#FFA15A'],
        mapbox_style="carto-positron",
        height= 700,
    )
    st.plotly_chart(fig, use_container_width=True)
with col2:
    #opis wykresu year count
    st.header('')
    st.header('Mapa wszystkich uderzeń', divider='grey')
    st.markdown('''  
    Mapa na której zaznaczone są punkty rejestrowanych uderzeń meteorytów na Ziemię.  
    Każdy punkt na mapie symbolizuje konkretne zdarzenie, posiadając nazwę związaną z meteorytem, który spadł.  
    Po najechaniu kursorem na dany punkt, można uzyskać informacje o współrzędnych geograficznych miejsca, w którym doszło do uderzenia oraz o nazwie meteorytu.
    ''')
st.divider()
tab1, tab2 = st.tabs(["Wykres", "Kod"])
with tab1:
    col1, col2 = st.columns([0.7, 0.3])
    with col1:
        # Filtracja danych po krajach
        sorted_df_countries = df_countries["country"].value_counts().reset_index()
        sorted_df_countries.columns = ['country', 'count']

        options = st.multiselect(
            'Wybierz Państwo lub Antarktykę (posortowane rosnąco od ilości wystąpień)', 
            options=sorted_df_countries['country'], default="Poland"
        )

        selected_countries_df = df_countries[df_countries['country'].isin(options)]
        fig = px.scatter_mapbox(
            selected_countries_df,
            lat="reclat", 
            lon="reclong",
            hover_name="name",
            zoom=0.7,
            center=dict(lon=0, lat=0),
            color_discrete_sequence=['#FFA15A'],
            mapbox_style="carto-positron",
            height= 700,
        )
        st.plotly_chart(fig, use_container_width=True)
with tab2:
    #opis wykresu fall count
    st.markdown('''
Dane pobrane ze strony NASA pierwotnie nie mają w sobie zaszytej informacji o tym w którym kraju znaleziono dany obiekt. Jest to ważne z punktu widzenia analizy i wizualizacji.
Ten kod ma na celu przypisanie nazw krajów do danych o uderzeniach meteoroidów na Ziemię, które są przechowywane w pliku CSV. Kod korzysta z biblioteki pandas do manipulacji danymi oraz geopy do geolokalizacji, zwłaszcza do odwzorowywania nazw krajów na podstawie współrzędnych geograficznych (szerokości i długości geograficznej).
Ogólny opis kroków:
- Wczytanie danych z pliku CSV, a następnie usunięcie wierszy, w których współrzędne geograficzne są równe 0 lub mają brakujące wartości.
- Inicjalizacja obiektu geolokalizatora za pomocą biblioteki geopy.
- Zdefiniowanie funkcji get_country_name, która przyjmuje wiersz danych i wykorzystuje geolokalizację do uzyskania nazwy kraju na podstawie współrzędnych. Nazwa kraju jest następnie przypisywana do nowej kolumny 'country' w ramce danych.
- Pętla po danych w ramce danych, w której dla każdego wiersza wywoływana jest funkcja get_country_name. Przypisane nazwy krajów są zapisywane w kolumnie 'country'.
- W trakcie przetwarzania, co 100 wierszy, wyniki są zapisywane do plików CSV, aby monitorować postęp. Pomiędzy iteracjami jest dodane opóźnienie 1 sekundy, aby uniknąć zbyt częstego zapytywania geolokalizatora.
- Po zakończeniu przetwarzania wszystkie wyniki są zapisywane do ostatecznego pliku CSV o nazwie 'Meteorite_Landings_Countries.csv'.
''')
    code = '''
import pandas as pd
from geopy.geocoders import Nominatim
import time

# Wczytanie pliku CSV
file_path = 'Meteorite_Landings.csv'
# Usuń wiersze, w których 'lat' lub 'lon' są równe 0 i są wartości null
df = pd.read_csv(file_path)
df = df.dropna(subset=['reclong', 'reclat'])
df = df[(df['reclong'] != 0) & (df['reclat'] != 0)]

# Inicjalizacja obiektu geolokalizatora
geolocator = Nominatim(user_agent="Wojciech")

# Funkcja do przypisywania nazwy kraju na podstawie współrzędnych
def get_country_name(row):
    location = geolocator.reverse(f"{row['reclat']}, {row['reclong']}", language='en')
    if location and location.raw.get('address'):
        return location.raw['address'].get('country')
    return None

# Dodanie kolumny 'country' do przechowywania nazw krajów
df['country'] = None

# Licznik do śledzenia postępu
counter = 0

# Pętla po danych w DataFrame
for index, row in df.iterrows():
    df.at[index, 'country'] = get_country_name(row)
    
    counter += 1
    
    # Zapisywanie wyników co 100 wierszy
    if counter % 100 == 0:
        output_file = f'wyniki_{counter}.csv'
        df.head(counter).to_csv(output_file, index=False)
        print(f"Zapisano {counter} wyników do pliku: {output_file}")
    
    # Oczekiwanie 1 sekundy przed kolejnym zapytaniem
    time.sleep(1)

# Ostatni zapis
output_file = 'Meteorite_Landings_Countries.csv'
df.to_csv(output_file, index=False)

print(f"Wszystkie wyniki zostały zapisane do pliku: {output_file}")

# Wczytaj plik CSV
df = pd.read_csv('Meteorite_Landings_Countries.csv')

# Dodaj wartość "Antarctic" do wierszy, gdzie wartość w kolumnie 'lat' jest mniejsza niż -60
df.loc[df['lat'] < -60, 'country'] = 'Antarctic'

# Zapisz zmieniony DataFrame z powrotem do pliku CSV
df.to_csv('zmieniony_plik.csv', index=False)
'''
    st.code(code, language='python')
