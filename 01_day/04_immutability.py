age = 39
print(age, id(age))

age = 18
print(age, id(age))

a = 10
b = a
print(id(a), id(b))

a = 1000
b = 1000
print(id(a), id(b))
b = 2000
print(id(a), id(b))
