# type string
str = "Hello World!"
print(str)
print(len(str))  # 12

print(str[0])  # h
print(str[3])  # l
print(str[len(str) - 1])  # !

subString = str[0:6]
print(subString)  # hello

str_x4 = subString * 4
print(str_x4)

otherStr = str + " and hello again!"
print(otherStr)

print(otherStr[7:])  # orld! and Hello Again!

print(otherStr[::2])  # HloWrd n el gi! - co drugi znak
print(otherStr[::3])  # -//- co trzeci

userName = input("Podaj swoje imie milordzie:")
print("Twoje imie to:", userName)

txt2 = """jeden
dwa
trzy"""
print(txt2)

txt3 = "jeden \ndwa \ntrzy"
print(txt3)
