# krotki

users = ("Ania", "Karol", "Marta", "Adam")
#users[0] = "Paweł"
print(users)
print(type(users)) # <class 'tuple'>
print(len(users)) # 4

emptyTuple = ()

digits = 1, 2, 3, 4, 5
print(type(digits)) # <class 'tuple'>
print(users[0])
print(users[-1])
print(users[0:3]) # ("Ania", "Karol", "Marta")
print(users[:2]) # ('Ania','Karol')

data = (("Ania", "Rafał"),("Asia","Karol"))
print(data[0][1]) # Rafał