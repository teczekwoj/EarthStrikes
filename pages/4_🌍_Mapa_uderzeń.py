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
            height= 770,
        )
        st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.header('Mapa obszarowa', divider='grey')
            st.markdown('''
            Na tej interaktywnej mapie dostępne są filtry krajów, pozwalające użytkownikowi skoncentrować się na uderzeniach meteoroidów w wybranych regionach świata.
            Interfejs umożliwia użytkownikowi wybór konkretnych krajów, które chce zobaczyć na mapie, co pozwala na bardziej spersonalizowane i ukierunkowane eksplorowanie danych o uderzeniach meteoroidów.
            Dodatkowo, po wybraniu obszaru pojawiają się informacje statystyczne.
            ''')
            percentage = (len(selected_countries_df)/len(df_countries))*100
            percentage_str = f"{percentage:.2f}%"
            st.metric(label=":orange[Ilość meteorytów znalezionych w wybranym kraju:]", value=len(selected_countries_df))
            st.metric(label=":orange[Procent wzystkich znalezionych meteorytów na Ziemi:]", value=percentage_str)
            st.dataframe(selected_countries_df,use_container_width=True, hide_index=True,height=280)

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
st.divider()
col1, col2 = st.columns([0.7, 0.3])

with col1:
    # Ustawienia kolorów dla mapy
    color_scale = [(0, 'lightblue'), (1, 'darkblue')]

    # Zakresy mas zdefiniowane w kodzie aplikacji
    mass_ranges = {
        1: (0, 100),
        2: (101, 1000),
        3: (1001, 10000),
        4: (10001, 1000000),
        5: (1000001, df['mass (g)'].max())
    }

    # Wybór zakresu mas meteorytów za pomocą slidera
    selected_range = st.slider(
        'Wybierz zakres mas meteorytów',
        min_value=1, max_value=5, step=1, 
    )

    # Pobranie zakresu mas na podstawie wybranej wartości ze slidera
    mass_range_options = mass_ranges[selected_range]

    # Filtracja danych po zakresie mas
    selected_mass_range_df = df[(df['mass (g)'] >= mass_range_options[0]) & (df['mass (g)'] <= mass_range_options[1])]

    coll1, coll2, coll3 = st.columns([0.4,0.4,0.4])
    with coll1:
        # Obliczenia procentowej masy z danego zakresu
        percentage_mass_range = (selected_mass_range_df['mass (g)'].sum() / df['mass (g)'].sum()) * 100
        # Wyświetlenie metryki
        st.metric(label=":orange[Masa zakresu/masa całkowita]", value=f"{percentage_mass_range:.2f}%")
        st.info("""Wartości zakresów:  
                1. od 1g do 100g  
                2. od 101g do 1000g (1kg)  
                3. od 1kg do 10kg  
                4. od 10kg do 1000kg (1t)  
                5. od 1t do masy największego meteoru
        """)
    with coll2:
        percentage_quantity_range_1 = (selected_mass_range_df.shape[0] / df.shape[0]) * 100
        st.metric(label=":green[Ilość zakresu/ilość całkowita]", value=f"{percentage_quantity_range_1:.2f}%")
    with coll3:
                # Pobranie zakresu mas na podstawie wybranej wartości ze slidera
        mass_range_options = mass_ranges[selected_range]

        # Filtracja danych po zakresie mas
        selected_mass_range_df = df[(df['mass (g)'] >= mass_range_options[0]) & (df['mass (g)'] <= mass_range_options[1])]

        # Obliczenia średniej masy meteorytu z zakresu
        average_mass_range = selected_mass_range_df['mass (g)'].mean()

        # Konwersja średniej masy do kilogramów i ton
        average_mass_kg = average_mass_range / 1000
        average_mass_ton = average_mass_kg / 1000

        # Wyświetlenie metryk w różnych jednostkach
        st.metric(label=":blue[Uśredniona masa w gramach]", value=f"{average_mass_range:.2f} g")
        st.metric(label=":purple[Uśredniona masa w kilogramach]", value=f"{average_mass_kg:.2f} kg")
        st.metric(label=":red[Uśredniona masa w tonach]", value=f"{average_mass_ton:.4f} ton")
            # Tworzenie interaktywnej mapy
    fig = px.scatter_mapbox(
        selected_mass_range_df,
        lat="reclat",
        lon="reclong",
        hover_name="name",
        zoom=0.7,
        center=dict(lon=0, lat=0),
        color="mass (g)",
        color_continuous_scale=color_scale,
        mapbox_style="carto-positron",
        height= 770
    )

    # Wyświetlenie mapy
    st.plotly_chart(fig,use_container_width=True)

with col2:
            st.header('')
            st.header('')
            st.header('')
            st.header('Mapa mas', divider='grey')
            st.markdown('''
            Interaktywna mapa na stronie internetowej przedstawiająca znalezione meteoryty stanowi heatmap zależny od mas tych obiektów.
            Użytkownik ma możliwość wyboru mapy z pięciu dostępnych zakresów mas meteorytów. Dodatkowo, na mapie widoczne są wskaźniki takie jak:
            - procentowa masa danego zakresu w stosunku do masy całkowitej, 
            - procentowa ilość meteorytów w danym zakresie w stosunku do ilości całkowitej, 
            - uśredniona masa pojedynczego meteorytu w danym zakresie.
                        
            To narzędzie umożliwia użytkownikowi dynamiczne eksplorowanie i analizę danych dotyczących znalezionych meteorytów.
            ''')
            st.dataframe(selected_mass_range_df,use_container_width=True, hide_index=True,height=480)

