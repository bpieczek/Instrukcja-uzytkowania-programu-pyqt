# Generator 50 liczb pseudolosowych

## Strona tytułowa
![Strona tytułowa](strona_tytulowa.png)

## Spis treści
1. [Opis programu](#opis-programu)
2. [Instrukcja obsługi](#instrukcja-obsługi)
   - [Wybór zakresu liczb](#Wybór-zakresu-liczb)
   - [Obliczanie sumy](#Obliczanie-sumy)
   - [Wyszukiwanie maksimum](#Wyszukiwanie-maksimum)
   - [Wyszukiwanie minimum](#Wyszukiwanie-minimum)
   - [Sortowanie liczb](#Sortowanie-liczb)
3. [Zabezpieczenia](#Zabezpieczenia)

## Opis programu
Generator 50 liczb pseudolosowych to prosta aplikacja desktopowa, która generuje, zlicza, sortuje i wyświetla losowe liczby. Aplikacja jest napisana w języku Python za pomocą biblioteki PyQt. Aplikacja po uruchomieniu zawiera:
1. Etykiete z nazwą programu czyli: "Generator 50 liczb pseudolosowych"
2. Etykiete z napisem: "Podaj zakres"
3. Pole edycyjne z Etykietą Minimum
4. Pole edycyjne z Etykietą Maksimum
5. Przyciek o nazwie generuj
6. 4 przyciski z etykietami kolejno
   - Etykieta o nazwie "Suma" i przycisk o nazwie "Sumuj"
   - Etykieta i przycisk o nazwie "Minimum"
   - Etykieta i przycisk o nazwie "Maksimum"
   - Etykieta o nazwie "Pierwsze 15 posortowanych liczb" i przycisk o nazwie "Sortuj"

Program po uruchomieniu:

![aplikacja po uruchowmniniu](assets/AplikacjaPoUruchomieniu.png)

## Instrukcja obsługi

### Wybór zakresu liczb
1. Wprowadź dolną i górną granicę zakresu liczb w polach edycyjnych.
2. Kliknij przycisk "Generuj", aby wygenerować 50 losowych liczb z wybranego zakresu.

![Wybór zakresu liczb](assets/WyborZakresu.png)

### Obliczanie sumy
1. Kliknij przycisk "Sumuj", aby obliczyć sumę wygenerowanych liczb.
2. Wynik zostanie wyświetlony obok etykiety "Suma".

![Obliczanie sumy](obliczanie_sredy.png)

### Wyszukiwanie maksimum
![Wyszukiwanie maksimum](wyszukiwanie_maksimum.png)

1. Kliknij przycisk "Max", aby znaleźć największą liczbę w wygenerowanym zestawie.
2. Wynik zostanie wyświetlony na ekranie.

### Wyszukiwanie minimum
![Wyszukiwanie minimum](wyszukiwanie_minimum.png)

1. Kliknij przycisk "Min", aby znaleźć najmniejszą liczbę w wygenerowanym zestawie.
2. Wynik zostanie wyświetlony na ekranie.

### Sortowanie liczb
![Sortowanie liczb](sortowanie_liczb.png)

1. Kliknij przycisk "Sort", aby posortować wygenerowane liczby.
2. Pierwsze 15 liczb zostanie wyświetlonych na ekranie.

### Zabezpieczenia
Aplikacja ma zabezpieczenia, które uniemożliwiają obliczanie sumy, wyszukiwanie maksimum i minimum, jeśli liczby nie zostały jeszcze wygenerowane, w przypadku podania niepoprawnych liczb, oraz w przypadku kiedy maksimum będzie większe od minimum. W takim przypadku, wyświetlany będzie komunikat ostrzegawczy.

Komunikat w przypadku braku podanego zakresu liczb lub w przypadku podaniu nieprawidłowych liczb (liczb lub znaków sepcjalnych):

![Komunikat Zle Liczby](assets/KomunikatZleLiczby.png)

Komunikat w przypadku próby sumowania, szukania minimum lub maksimum, lub sortowania przy jednoczesnym braku wygenerowanych liczb:

![Komunikat Brak Wygenerowanych Liczb](assets/KomunikatBrakWygenerowanychLiczb.png)

Komunikat w przypadku kiedy Minimum jest większe od Maksimum:

![Minimum większe od Maksimum](assets/MinWiekszeOdMax.png)
