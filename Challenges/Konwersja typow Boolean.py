# Konwersja na bool
# Fukncja bool() przeksztalca wartosc na wartosc logiczna czyli typ Boolean ktory moze przyjmowac jedna z dwoch
# Wartosci: True lub False reprezentujacych prawde lub falsz

# ponizej wartosci ktore daja False tzw Falsy values
print(bool())
print(bool(False))  # False
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(()))  # false
print(bool([]))  # false
print(bool({}))  # false
print(bool(""))  # pusty lancuch znakow daje False
print(bool(None))  # None oznacza brak przypisanej wartosci, rowniez konwertuje na False

# Metoda bool() konwertuje warosc do wartosci logicznej czyli Boolean ktory moze przyjac True albo False
# tzn. prawde albo falsz
print("_______________________")
# ponizej wartosci ktore daja true
print(bool(True))  # true
print(bool(1))  # true
print(bool(5))  # true
print(bool(-10))  # true
print(bool(("Ola", 1)))  # krotka z przynajmniej jednym elementem True
print(bool([0]))  # listy z przynajmniej jednym elementem daja True
print(bool({0}))  # zbiory z przynajmniej jedenm elementem daja True
print(bool("x"))  # String z przynajmniej jednym znakiem daja True
