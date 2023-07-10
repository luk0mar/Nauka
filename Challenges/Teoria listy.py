# Typ list
brands = ["Sony", "Dodge", "Ford", "Citroen"]
print(type(brands[0])) #<class 'list'>
print(brands[0]) # sony
print(brands [ len(brands) -1 ]) # citroen

print(brands[-1]) # citroen
print(brands[-3]) # "dodge"
print(brands[0:2]) # ['Sony', 'Dodge']
print(brands[0:3]) # ['Sony', 'Dodge', 'Ford']
print(brands[1:]) # Dodge ford citroen
print(brands[:3]) # sony dodge ford
print(brands[:4]) # sony dodge ford citoren

brands[1] = "Mercedes"
print(brands)

#brands[4] = "GMC" # indexError

brands.append("GMC") # dodanie nowej marki
print(brands)

brands.insert(0, "Lenovo")
print(brands) # ['Lenovo', 'Sony', 'Mercedes', 'Ford', 'Citroen', 'GMC']

print("Sony" in brands) # true
print("Bmw" in brands) #false bo bmw nie ma:)

if "Sony" in brands:
    print("Sony jest na liście")

del brands[2] # del usuwa pozycje z listy :) 
print(brands)
