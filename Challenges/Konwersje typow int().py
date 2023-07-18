# Konwersje typow int()
# W niektorych przypadkach moze wystapic potrzeba konwersji typow danych co mozna osiagnac
# za pomoca odpowiednich funkcji. Aby przeksztalcic zmienna na liczbe calkowita nalezy uzyc metody int()

floatNumber = 12.3  # przykladowa liczba zmiennoprzecinkowa
print(type(floatNumber))  # <class 'float'>

intNumber = int(floatNumber)  # konwersja liczby float na liczbe int
print(intNumber)  # 12
print(type(intNumber))  # <class "int">

x = int(5)  # przykladowa liczba calkowita
y = int("32")  # konwersja ciagu znakow na liczbe calkowita
print(type(y))  # <class 'int'>
