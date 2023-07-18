numberSet = {2, 3, 1, 4, 5}
numberSet.add(22)
numberSet.add(30)
numberSet.add(30)
numberSet.add(30)
numberSet.add(22)

numberSet.discard(1)
print(type(numberSet))
print(numberSet)

for v in numberSet:
    print(v)

frozenSetNumber = frozenset(numberSet)
print(type(frozenSetNumber))  # <class 'frozenset'>

for v in frozenSetNumber:
    print(v)
