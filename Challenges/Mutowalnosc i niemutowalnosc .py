# Mutowalnosc vs niemutowalnosc
# W Pythonie typy danych mozna podzielic na dwie kategorie: mutowalne i niemutowalne
# Mutowalne typy pozwalaja na zmiane wartosci podczas gdy niemutowalne tego nie umozliwiaja

# W analizie wykorzystamy specjalna funkcje id() ktora zwraca unikatowy identyfikator
# dla kazdego podanego obiektu. W praktyce jest to liczba calkowita wskazujaca miejsce
# w pamieci gdzie przechowywana jest wartosc. Nalezy pamietac ze w Pythonie wszystko jest
# obiektem w tym liczby calkowite, libczy zmiennoprzecinkowe, krotki itp

a = 10
b = 20

print(id(a))
print(id(b))
print(id(a) == id(b))  # false

# Mutowalnosc vs niemutowalnosc cz.2
# Nastepny przyklad ilustrujne niemutowalnosc liczb calkowitych, a podobnie zachowuja sie liczby
# Zmiennoprzecinkowe, wartosci logiczne, ciagi znakow, krotki oraz frozensety ktorych wartosci
# nie mozna zmienic. Wszelkie operacje na nich generuja nowa wartosc w pamieci Funkcja id()
# ktora wraca tozsamosc obiektu czyli jego adrss w pamieci, pozwala to zobaczyc

a = 1
addr1 = id(a)

a += 1  # zwiekszenie o 1
addr2 = id(a)

print(addr1)
print(addr2)
print(addr1 == addr2)  # false

# Modyfiakcja wartosci zmiennej "a" spowodowala utworzenie nowej liczby calkowitej
# w pamieci z nowa wartoscia 2. Zmienna "a" wskazuje teraz na te nowa wartosc.
# Oryginalny obiekt liczby calkowitej nie mogl zostac zmieniony, poniewaz jest niemutowalny
# co doprowadzio do stworzenia nowego obiektu w pamieci.
