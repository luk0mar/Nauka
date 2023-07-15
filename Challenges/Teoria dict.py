# dict - slownik, zbior par kluczy oraz wartosci, klucze musza byc unikalne
# sluza do pobrania wartosci. Elementy w slowniku nie maja kolejnosci.
# To nie jest lista!

contacts = {
    "Ania": "ania@example.com",
    "Daniel": "daniel@example.com",
    "Ola": "ola@example.com",
}

contacts["Olek"] = "olek@example.com"

print(len(contacts))  # 4
print(contacts["Ania"])  # ania@example.com
print(contacts["Olek"])  # olex@example.com

print(contacts.keys())  # klucze dostepne w slowniku
print(contacts.values())  # wartosci dostepne w slowniku
