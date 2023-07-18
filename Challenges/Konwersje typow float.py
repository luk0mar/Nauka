# w celu przeksztalcenia zmiennej na liczbe zmiennoprzecinkowa nalezy uzyc metody float()

intNumber = 20
print(type(intNumber))  # <class "int">

floatNumber = float(intNumber)  # konwesja liczby calkowitej na liczbe float
print(floatNumber)  # 20.0
print(type(floatNumber))  # <class "float">

f = float("76.789")
print(f)  # 76.789
print(type(f))  # <class "float">

# nieprawidlowa liczba w lancuchu powoduje blad
# float("123,34") # valuerror
