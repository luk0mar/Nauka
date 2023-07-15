# 1. Stworz krotke lastExpenses z ostatnimi wydatkami na koncie bankowym z wartosciami: 200, 300, 400, 500, 600
# 2. Policz wydatki za pomoca petli for i wyswietl w konsoli ostateczna kwote. Pamietaj aby stworzyc zmienna
# z wartoscia poaczatkowa 0 do ktorej dodasz kolejny wydatek

lastExpenses = 200, 300, 400, 500, 600
result = 0
for value in lastExpenses:
    result = result + value

print("Suma wydatków:", result)
