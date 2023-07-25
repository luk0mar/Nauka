# Obiekty mutowalne moga byc zmienione z zachowaniem tego samego miejsca w pamieci

listData = ["a", "b"]
addr1 = id(listData)

listData += ["c", "d"]
addr2 = id(listData)
print(addr1)
print(addr2)
print(addr1 == addr2)
