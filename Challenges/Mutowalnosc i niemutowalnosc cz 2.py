# Taka sama sytuacja bedzie z innymi niemutowalnymi obiektami oprocz int czyli np float,
# str, tuple

f = 3.2
addr1 = id(f)

f = f + 2.5
addr2 = id(f)

print(addr1)
print(addr2)
print(addr1 == addr2)
