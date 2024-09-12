a = 10
b = 10
print(a == b)
print(id(a) == id(b))
print(a is b)

c = [1, 2, 3]
d = [1, 2, 3]
print(c == d)
print(id(c) == id(d))
print(c is d)


grades = [1, 2, 3, 4, 5]
for grade in grades:
    if grade != 3:
        print(grade)


# for ciklusváltozó in szekvencia:
#     ciklusmag

# for ciklusváltozó in range(kezdet, vége, lépésköz):
#     ciklusmag

# ciklusvaltozo = kezdőérték
# while feltétel:
#     ciklusmag
#     ciklusvaltozo = lépésköz

for i in range(10):
    print(i)

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# while True:
#     grade = input("Please provide your grade: ")
#     if grade.isdigit() and 1 <= int(grade) <= 5:
#         print("This is a grade")
#         break
#     else:
#         print("THIS IS NOT A GRAAAAADEEEE!!!")


number = 525
i = 2

while i <= number // 2:
    if number % i == 0:
        print("This is not a prime")
        break
    i += 1
else:
    print("This is a prime")
