floatNumber = 47.2345
intNumber = int(floatNumber)
print(type(intNumber))  # class int
print(intNumber)

float2 = float(12345)
print(type(float2))  # class float
print(float2)

int2 = int(" 567")
print(type(int2))  # class int
print(int2)

float3 = float(" 567.5465 ")
print(type(float3))  # class float
print(float3)  # 567

print("liczba int to: " + str(int2))
print("liczba float to: " + str(float3))
print("liczba float to: ", float3)
