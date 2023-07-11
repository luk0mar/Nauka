# krotka - uporzadkowany ciag danych, niemodyfikowalny zbior 
# utworzony za pomoca nawiasow okraglych i elementow oddzielonych przecinkami.
# Krotke mozna latwo wyobrazic sobie jako pojedynczy rekord w bazie danych dotyczacy uzytkownika
# obejmujacy informacje takie jak login, email, date rejestracji itp.

numberNames = ("jeden", "dwa", "trzy")
print(type(numberNames)) # <class "tuple">
print(numberNames)  # ("jeden", "dwa", "trzy")

# krotka moze byc stosowana rowniez bez nawiasow
brands = "Motorola", "apple", "google"
print(type(brands))

# pusta krotka musi miec nawiasy!
emptyTuple = ()
print(type(emptyTuple))

# krotka zawierajaca tylko jedna wartosc musi zawierac przecinek po tym elemencie
# co wskazuje na to ze chcemy utworzyc kortke a nie ciag znakow
fighters = ("F15",)
print(type(fighters))

# odczyt danych opiera sie na tych samych zasadach co w przypadku list co oznacza
# ze mozna korzystac z indeksow dodatnich oraz ujemnych
words = ("jeden", "dwa", "trzy", "cztery", "piec", "szesc")
print(words[1]) # dwa
print(words[1:4]) # ("dwa", "trzy", "cztery")
print(words[-1]) # szesc
print(words[-5]) # dwa
print(words[4:]) #("piec", "szesc") od czwartego elementu
print(words[::2]) # ("jeden", "trzy", "pięć") co drugi element

# krotka wielopoziomowa/wielowymiarowa
nestedTuple = ((1, 2, 3, ), words) # krotka wielowymiara, dwie krotki w jednej
print(nestedTuple[0][1]) # 2

# krotka jest niemutowalna - nie moze byc modyfikowana 
textTuple = ("Apple", "Banana", "orange")
# textTuple[10] = "grape" #TypeError: 'tuple' object does not support item assignment

# krotki mozna laczyc dzieki konkatenacji:
tuple1 = (10, 20, 30)
mergedTuples = tuple1 + (40, 50, 60)
print(mergedTuples) # (10, 20, 30, 40, 50, 60)

# operator in pozwala na sprawdzenie czy wartosc jest w kortce
# dziala rowniez w petli for in:
print(20 in (10,20,30)) #true

for value in (100, 200, 300):
    print(value)

# krotki mozna usuwac uzywajac slowa kluczowego "del"
numTuple = (11, 22, 33, 44)
print(numTuple)
del numTuple # usuwanie krotki
# print(numTuple) # - Błąd, odkomentowanie tej lini spowoduje blad poniewaz krotka zostala wczesniej usunieta

# proba usuniecia elementu w krotce spowoduje blad gdyz jest niemutowalna
anotherTuple = (100, 200, 300)
# del anotherTuple[0]  # blad! odkomentowanie tej linii spowoduje blad
# poniewaz krotki sa niemutowalne

