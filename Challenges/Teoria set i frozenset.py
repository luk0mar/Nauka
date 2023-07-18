# set - zestaw to nieuporzadkowany zbior unikalnych wartosci
# Zbior w pythonie nie pozwala na dodawanie zduplikowanych elementow, jest iterowalny, modyfikowalny,
# ale nie ma indeksow dla elementow. Istnieje wariant tego obiektu zwany frzenset ktory jest niemodyfikowalny.
# Zbiory sa zapisywane za pomoca nawiasow klamrowych i oddzielonych przecinkami wartosci

numberSet = {0, 4, 8, 12, 16}  # inicjalizacja zbioru

numberSet.add(20)  # dodanie elementu do zbioru
print(numberSet)
numberSet.add(20)  # dodanie zostalo zignorowane

numberSet.discard(8)  # usuniecie 8
print(numberSet)

for value in numberSet:  # iterowanie po zbiorze
    print(value)

# frozenset  - niemutowalny zestaw to nieuporzadkowany zbior unikalnych wartosci
# forzenset jest podobny do zbioru ale rozni sie tym ze po utworzeniu nie mozna go modyfikowac

exampleSet = {2, 6, 10, 14, 18}  # inicjalizacja zbioru
exampleSet.add(26)  # dodanie do elementu zbioru

frozenExampleSet = frozenset(exampleSet)  # tworzenie niemodyfikowalnego zbioru
print(frozenExampleSet)
# frozenExampleSet.add(30) # blad - niemozliwe jest dodanie elementu do frozenset

for value in frozenExampleSet:
    print(value)
