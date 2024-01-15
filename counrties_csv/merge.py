import pandas as pd

# Wczytaj pliki CSV
df1 = pd.read_csv('Meteorite_Landings=.csv')
df2 = pd.read_csv('Meteorite_Landings_Countries.csv')

# Połącz ramki danych na podstawie warunku
merged_df = pd.merge(df1, df2, left_on=['reclat', 'reclong'], right_on=['lat', 'lon'], how='left')

# Dodaj wartość z kolumny 'country' do pliku 1, gdzie warunki są spełnione
merged_df['country_x'] = merged_df['country_x'].fillna(merged_df['country_y'])

# Usuń niepotrzebne kolumny z ramki danych wynikowej
merged_df = merged_df.drop(['lat', 'lon', 'country_y'], axis=1)

# Zapisz zmieniony DataFrame z powrotem do pliku CSV
merged_df.to_csv('polaczony_plik.csv', index=False)
