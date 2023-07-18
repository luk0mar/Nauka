# Konwersje typow - tuple() oraz list()
# Konwersja na krotke:
listData = [1, 2, 3, 4]
tupleData = tuple(listData)  # z listy na krotke
print(tupleData)  # <class "tuple">

# Konwersja na liste
tuple2 = ("Ola", "Adam")
newList = list(tuple2)  # krotka na liste
print(type(newList))  # <class "list">
