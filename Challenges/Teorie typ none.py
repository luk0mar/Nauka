# Typ none oznacza brak wartości np. ze zmienna nie posiada
# przypisanej wartosci - cos jak null w innych jezykach programowania

data = None
print(type(data))  # <class "NoneType">

if data is True:
    print("Data is true")
elif data is False:
    print("Data is false")
else:
    print("None is none")
