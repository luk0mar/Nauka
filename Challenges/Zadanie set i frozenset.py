# 1. Stworz set z unikalnymi wartosciami jak:
# Toyota, Honda, BMW, Mercedes, Audi, Ford
# 2. Dodaj do set za pomoca funkcji kolejne elementy:
# Volkswagen, Mazda, BMW, Mercedes, Audi, Chevrolet
# 3. Pokaz w konsoli wielkosc set
# 4. Wykorzystaj petle for aby pokazac elementy w set

numberSet = {"Toyota", "Honda", "BMW", "Mercedes", "Audi", "Ford"}
numberSet.add("Volskwagen")
numberSet.add("Mazda")
numberSet.add("BMW")
numberSet.add("Mercedes")
numberSet.add("Audi")
numberSet.add("Chevrolet")

print(len(numberSet))

for v in numberSet:
    print(v)
