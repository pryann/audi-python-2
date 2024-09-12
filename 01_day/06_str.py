firstname = "Gergely"
lastname = "Gáll"
fullname = firstname + " " + lastname
print(fullname)
print("hello" * 10)

age = 18
about_me = (
    "My name is " + firstname + " " + lastname + " and I am " + str(age) + " years old."
)

print(about_me)

about_me = "My name is {0} {1} and I am {2} years old.".format(firstname, lastname, age)
print(about_me)

about_me = f"My name is {firstname} {lastname} and I am {age + 12} years old."
print(about_me)

PI = 3.14159265359
print("Formated PI: {0:.2f}".format(PI))

print(r"First line \nSecond line")

job = "mentor"
print(job.upper())
print(job)

print(job[0])
print(job[5])
# IndexError: string index out of range
# print(job[6])
print(job[-1])
print(job[-2])
# job[0] = "M"

abc = "abcdefghij"
print(abc[0:2])
print(abc[0:6:2])
print(abc[0::2])
print(abc[-1::-1])

abc_copy = abc[:]
print(abc_copy)
