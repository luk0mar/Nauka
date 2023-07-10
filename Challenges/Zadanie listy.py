# 1. Stwórz listę numberList z kolejnymi liczbami: od 5 do 15
# 2. Pokaż w konsoli długość listy, usuń 4 element i pokaż długość listy ponownie
# 3. Użyj instrukcji warunkowe if z in do sprawzenia czy liczba 9 jest w liście numberList
# Pokaż informacje w konsoli jeśli zachodzi taka sytuacja
# 4. Użyj pętli for aby pokazać wartości w liście pomniejszone o 5.
# 5. Użyj pętli for aby przejść po elemntach listy ale pokaż ich wartości podzielone przez 3

# 1.
numberList = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Długość listy", len(numberList))
del numberList[4]
print("Długość listy", len(numberList))

# 2.
if "9" in numberList:
    print("9 jest na liście")

# 3.
print("Wartości w liście pomnijeszone o 5: ")
for value in numberList:
    print(value  -5) 

print("Wartości w liście podzielone przez 3: ")
for value in numberList:
    print(value / 3)
