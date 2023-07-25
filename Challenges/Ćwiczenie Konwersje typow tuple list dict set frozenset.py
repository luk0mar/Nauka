numberList = [7, 8, 9, 10, 11, 12]

tupleData = tuple(numberList)
print(tupleData)
print(type(tupleData))  # <class 'tuple'>

list = list(("Ewa", 12, 15))
print(list)
print(type(list))  # <Class 'list'>

setData = set((1, 1, 2, 3, 4, 4, 5, 6))
print(setData)  # {1, 2, 3, 4, 5, 6}
print(type(setData))  # <class 'set'>

frSet = frozenset(setData)
print(frSet)
print(type(frSet))  # <class 'frozenset'>

contactsTuple = (
    ("Ola", "ola@example.com"),
    ("Ania", "ania@example.com"),
    ("Karol", "karol@example.com"),
)
contacts = dict(contactsTuple)
print(contacts)
print(type(contacts))  # <class 'dict'>
