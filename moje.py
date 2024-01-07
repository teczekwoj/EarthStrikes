import pandas as pd
from geopy.geocoders import Nominatim
import time

# Wczytanie pliku CSV
file_path = 'Meteorite_Landings.csv'  # Zmień na ścieżkę do swojego pliku
df = pd.read_csv(file_path)
df = df[['reclong', 'reclat']]
df = df.dropna(subset=['reclong', 'reclat'])
df = df.rename(columns={'reclong': 'lon', 'reclat': 'lat'})

# Inicjalizacja obiektu geolokalizatora
geolocator = Nominatim(user_agent="Wojciech")

# Funkcja do przypisywania nazwy kraju na podstawie współrzędnych
def get_country_name(row):
    location = geolocator.reverse(f"{row['lat']}, {row['lon']}", language='en')
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
output_file = 'wyniki.csv'
df.to_csv(output_file, index=False)

print(f"Wszystkie wyniki zostały zapisane do pliku: {output_file}")
