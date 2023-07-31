# Manipulacja wartosciami i zmiennymi jest mozliwa dzieki operatorom. Operatory
# arytmetyczne umozliwiaja przeprowadzenie obliczen matematycznych

a = 10
b = 6

result = a + b  # 16
result = a - b  # 4
result = a * b  # 60
result = a / b  # 1.66 dzielenie zawsze zwraca wartosc zmiennoprzecinkowa
result = a % b  # reszta z dzielenia 4
result = a**b  # 10 do potegi 4
result = 20 // 3  # dzielenia dajace tylko liczbe calkowita jako wynik: 6


# Operatory przypisania - maja na celu przypisanie wartosci zmiennym,
# jednoczesnie wykonujac dodatkowe dzialania matematyczne

numA = 8  # operator przypisania wartosci 8 do zmiennej numA
numB = 5

numA += 3  # to samo co numA = numA + 3 czyli numA = 11
numA -= 2  # numA = numA - 2, czyli numA = 9
numA *= 4  # numA = numA * 4 czyli numA = 36
numA %= 7  # numA = numA % 7 czyli numA = 1 (reszta z dzielenia)
numA **= 3  # numA = numA ** 3 czyli numA = 1 (1 do potegi 3)
numA //= 2  # numA = numA // 2 czyli numA = 0 (dzielenie calkowite)
