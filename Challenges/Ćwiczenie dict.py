bestComputerByYear = {
    2001: "sony",
    2002: "ibm",
    2003: "compaq",
    2004: "Sun",
    2005: "sony",
    2006: "Lenovo",
}

bestComputerByYear[2007] = "microsoft"
print(bestComputerByYear)
print(bestComputerByYear[2001])  # sony
print(type(bestComputerByYear))  # <class 'dict'>
print(len(bestComputerByYear))  # 7

print(bestComputerByYear.keys())
print(bestComputerByYear.values())

for key in bestComputerByYear.keys():
    print("Key:", key, "Value:", bestComputerByYear[key])

for key, value in bestComputerByYear.items():
    print("Key:", key, "Value:", value)
