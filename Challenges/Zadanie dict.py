# Wymagania:
# 1. Stwórz zmienna config ktroa bedzie slownikiem z konfiguracja strony internetowej, zapisz w niej
# ponizsze klucze z wartoscia:
# -"website" z wartoscia "example.com"
# - "dbType" z wartoscia "sql"
# - "dbUser" z wartoscia "admin123"
# - "dbPassword" z wartoscia "pass123"
# 2. Pokaz ilosc elementow slownika w konsoli
# 3. Pokaz w konsoli warosc klcza "dboType" z slownika
# 4. Wykorzystaj petle for in aby przejsc po wszystkich elementach slownika i pokaz je w konsoli
# wg. formatu: "Klucz w config: website z wartoscia exmaple.com"

config = {
    "website": "example.com",
    "dbType": "sql",
    "dbUser": "admin123",
    "dbPassword": "pass123",
}
print("Ilosc elementow w slowniku:", len(config))
print("Wartosc klucz dbType:", config["dbType"])

for key in config.keys():
    print("Klucz w config:", key, config[key])

for key, value in config.items():
    print("Key:", key, "Value:", value)
