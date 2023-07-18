# Konwersje typow str()
# Aby skonwertowac zmienna na lancuch znakow stosuje sie funkcje str()

str1 = str("intNum")  # konwersja int na łańcuch znaków
print(str1)  # 20
print(type(str1))  # <class "str">

str2 = str(45.456)
print(str2)
print(type(str2))

print("Rok ma " + str(365) + " dni")  # OK
print("Rok ma " + 365 + " dni")  # blad
