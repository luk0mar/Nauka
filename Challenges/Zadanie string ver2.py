# 1. wykorzystaj funkcje input() wbudowaną w python do pobrania informacji od uzytkownika z konsoli.
# Popros uzytkownika o podanie imienia, ulubionego koloru, zwierzecia oraz hobby
# Zapisz te informacje w zmiennych name, favColor, favAnimal i hobby
# 2. Wyswietl w konsoli tekst podumowujacy pobrane dane np: "Nazywasz sie Adam, Twoj ulubiony kolor to niebieski
# ulubione zwierze to pies, a Twoje hobby to czytanie ksiazek"

name = input("Podaj swoje imie :")
favColor = input("Jaki jest twój ulubiony kolor:")
favAnimal = input("Jakie jest twoje ulubione zwierzę:")
hobby = input("Jakie jest twoje hobby:")
txt = "Nazywasz się " + name + ", Twój ulubiony kolor to " + favColor
txt = txt + ", ulubione zwierzę to " + favAnimal + " a Twoje hobby to " + hobby
print(txt)