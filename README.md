# Specyfikacja aplikacji do analizy danych uderzeń meteorytów w Ziemię.  

## 1. Wymagania biznesowe
1.1 **Opis projektu**
Celem projektu jest stworzenie aplikacji webowej do analizy danych uderzeń wszytkich zidentyfikowanych przez NASA obiektów w Ziemię. Aplilacja ma w czytelny, przystępny i nowoczesny sposób prezentować dane na temat obiektów, pokazywać statystyki i wizualizacje na podstawie zbioru danych dostarczonego przez organizacje NASA.

1.2 **Najważniejsze cele projektu**  
- Interaktywna aplikacja webowa w formie panelu (dashboardu)
- Dane źródłowe w formacie .csv
- Aplikacja w jasny i czytelny sposób ma przedstawiać statystyki i wizualizacje na temat uderzeń obiektów w Ziemię
- Celem analizy jest zauważenie zależności lub trendu wśród meteorytów
- Podstawowe metody statystyczne wykorzystane w projekcie to: średnia, mediana, liczba elementów zbioru, warości max i min, dominanta, wariancja, odchylenie standardowe, histogram, wykresy słupkowe, wykresy kołowe itp.

1.3 **Źródła danych**  
Źródłem danych jest portal organizacji kosmicznej NASA's Open Data Portal (https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh).
Dane pozyskane z tego portalu są kompletne, sprawdzone i ogólnodostępne co czyni je gotowymi do analizy.

1.4 **Harmonogram projektu**  
Analiza wymagań - 2 tygodnie  
Projektowanie systemu - 4 tygodnie  
Implementacja systemu - 12 tygodni  
Testowanie i wdrożenie - 4 tygodnie  
Utrzymanie i aktualizacja - stały proces  

## 2. Wymagania dotyczące danych i ich jakości  
2.1 **Źródła danych**  
- Dane są przechowywane w pliku .csv  
- Stan danych  jest aktualizowany co parę miesięcy i zależy on od wolonaryjnej chęci pracowników NASA  
- Jakość tych danych jest sprawdzona, dane są prawidłowo zmodelowane i ustrukturyzowane  
- Organizajcą odpowiedzialną za poprawność tych danych jest NASA Open Data Portal, dane są udostępnianie publicznie na postawie licencji Open Source
- Aktualnie zestaw danych ma 47,7 tyś. unikalnych wierszy i 10 kolumn. Każdy z wierszy to pojedyńcze uderzenie obiektu w Ziemię.
- Dane te z czasem będą się powiększać, ponieważ obiekty ciągle uderzeją w Ziemie.  

2.2 **Oczyszczanie danych**
Dane źródłowe bedą miały jednolity charakter i formę. Będą podzielone na 10 kolumn o różnych typach danych:
- name (text) 
- id (text)
- nametype (text)
- recclass (text)
- mass g (num)
- fall (text)
- year (DateTime)
- reclat (text)
- reclong (text)
- GeoLocation (location)

## 3. Wymagania funkcjonalne
3.1 Logowanie użytkownika:  
- Aplikacja powinna umożliwiać użytkownikom zarejestrowanie się i zalogowanie
- Po zalogowaniu użytkownik powinien mieć dostęp do swojego indywidualnego dashboardu

3.2 Import danych:  
- Użytkownik powinien mieć możliwość importowania zbioru danych w formacjie .csv
- Aplikacja powinna obsługiwać wczytywanie danych z lokalnego dysku użytkownika

3.3 Podgląd danych:  
- Aplikacja powinna umożliwiać użytkownikowi podgląd wczytanych danych w formie tabeli lub innej czytelnej struktury

3.4 Wizualizacje danych:  
- Aplikacja powinna oferować różne rodzaje wizualizacji danych, takie jak wykresy, histogramy, mapy cieplne itp
- Użytkownik powinien mieć możliwość interaktywnego manipulowania wizualizacjami, takimi jak przybliżanie, oddalanie, filtrowanie, zmiana typu wykresu itp.

3.5 Filtry i sortowanie:  
- Użytkownik powinien mieć możliwość zastosowania filtrów do danych, aby wyświetlić tylko interesujące go rekordy
- Aplikacja powinna umożliwiać sortowanie danych według wybranych kolumn

3.6 Statystyki i analiza:  
- Aplikacja powinna dostarczać różne statystyki i wskaźniki na podstawie dostępnych danych, takie jak sumy, średnie, mediany itp.
- Użytkownik powinien mieć możliwość generowania raportów i podsumowań dla wybranych danych

3.7 Reaktywność: 
- Aplikacja powinna być responsywna i umożliwiać płynne działanie, nawet przy dużej ilości danych
- Wszelkie zmiany w danych lub interakcje użytkownika powinny być odzwierciedlane w czasie rzeczywistym

3.8 Udostępnianie:  
- Użytkownik powinien mieć możliwość udostępniania swojego dashboardu innym osobom poprzez generowanie linku lub zapisywanie go jako plik

## 4. Wymagania niefunkcjonalne
4.1 Wydajność:  
- Aplikacja powinna być szybka i responsywna, zapewniając płynne doświadczenie użytkownika nawet przy dużej ilości danych
- Czas wczytywania danych i generowania wizualizacji powinien być minimalny

4.2 Łatwość użycia:  
- Interfejs użytkownika powinien być intuicyjny i łatwy w obsłudze, nawet dla osób bez doświadczenia w analizie danych
- Instrukcje i wsparcie użytkownika powinny być dostępne, aby ułatwić korzystanie z aplikacji

4.3 Kompatybilność:
- Aplikacja powinna być kompatybilna z różnymi przeglądarkami internetowymi i systemami operacyjnymi
- Powinna działać na różnych urządzeniach, takich jak komputery stacjonarne, laptopy, tablety i smartfony

4.4 Rozszerzalność:
- Aplikacja powinna być łatwo rozszerzalna, umożliwiając dodawanie nowych funkcji, wizualizacji i modułów analizy danych

4.5 Utrzymanie:
- Aplikacja powinna być łatwa w utrzymaniu, umożliwiając aktualizacje, naprawy błędów i wprowadzanie zmian w przyszłości

## 5. Proponowane technologie
- Główny język zastowsowany w projekcjie - Python
- Strona webowa stworzona na podstawie biblioteki Pythona - Streamlit
- Biblioteka NumPy do obliczeń numerycznych dla danych i wizualizacji
- Biblioteka Pandas służy do analizy danych i zarządzania danymi. Jest używana zwykle z NumPy i Matplotlib. Obsługuje pliki CSV, korzysta z ramki danych (DataFrame) i jest szczególnie przydatna w procesie przygotowania danych.
- Biblioteka SciPy wykorzystywana w projektach obejmujących różne obliczenia: matematyczne, statystyczne, inżynieryjne. Współpracuje z Matplotlib, NumPy, 
- Biblioteka Matplotlib do wizualizacji danych w języku Python. Umożliwia tworzenie histogramów, wykresów rozrzutu, słupkowych, kołowych, itp.
- Seaborn do wizualizacji danych opartą na Matplotlib i dostarcza metod do wizualizacji statystycznych. Jest zintegrowana z NumPy i Pandas. Ma funkcje do operowania na ramkach danych (DataFrame) i tablicach. Zawiera ogromny zbiór narzędzi do złożonej wizualizacji. Umożliwia rysowanie wykresów kołowych, histogramów, wykresów rozrzutu, słupkowych itp.
- Microsoft Azure do hostingu strony www.

## Autor
Wojciech Latko
