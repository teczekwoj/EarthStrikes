import pandas as pd

# Wczytaj plik CSV
df = pd.read_csv('Meteorite_Landings_Countries.csv')

# Dodaj wartość "Antarctic" do wierszy, gdzie wartość w kolumnie 'lat' jest mniejsza niż -60
df.loc[df['reclat'] < -60, 'country'] = 'Antarctic'

# Zapisz zmieniony DataFrame z powrotem do pliku CSV
df.to_csv('zmieniony_plik.csv', index=False)
