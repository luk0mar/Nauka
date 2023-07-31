# immutable (zmiana tworzy nowy element w pamieci): int, float, bool, str, tuple, frozen
# mutable (zmiana wartosci w tym samym miejscu w pamieci): list, set, dict

a = 10
addr1 = id(a)

a = a + 2
addr2 = id(a)

print(addr1)
print(addr2)
print(addr1 == addr2)  # false


list = [0, 1, 2]
addr1 = id(list)

list += [3, 4, 5]
addr2 = id(list)
print(addr1)
print(addr2)
print(addr1 == addr2)  # true
