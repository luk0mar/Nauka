# # wymagania:
# 1. Popros uzytkownika o wprowadzenie liczby calkowitej uzywajac input()
# Pamietaj ze input zwraca lancuch znakow wiec musisz ta wartosc od uzytkownika
# skonwertowac na faktyczna liczbe calkowita
# intStr = input("Wprowadz liczbe calkowita")
# intNum = int(intStr)
# 2. Popros uzytkownika o wprowdzenie liczby zmiennoprzecinkowej z input() zrob konwersje
#  str na float
# 3. Oblicz sume liczby calkowitej i skonwertowanej na int liczby zmiennoprzecinkowej
# 4. wyswietl wynik obliczen

intStr = input("Wprowadz liczbe calkowita: ")
intNum = int(intStr)

intStr2 = input("Wprowadz liczbe zniennoprzecinkowa: ")
intNum2 = float(intStr2)

sum = intNum + int(intNum2)
print("Suma liczb: ", sum)
