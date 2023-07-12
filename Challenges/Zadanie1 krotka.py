# 1. Stworz krotke tupleValues z wartosciami: 20, 40, 60, 80, 100, 120, 140
# 2. Pokaz typ krotki w konsoli
# 3. Pokaz w konsoli ilsc elemntow krotki
# 4. Pokaz ostatni element krotki wykorzystujac len() -1
# 5. Nastepnie pokaz elementy od drugiego do szóstego
# 6. Pokaz trzeci element od konca z ujemnym indeksem

tupleValues = (20, 40, 60, 80, 100, 120, 140)
print(type(tupleValues))
print(len(tupleValues))
print("Ostatni element kortki:", tupleValues[len(tupleValues)-1])
print(tupleValues[2:7])
print(tupleValues[-3])