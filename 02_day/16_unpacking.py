abc = "abcdefghijklmnop"

a, b, c, *others = abc
print(a, b, c, others)

person = ["John", "Doe", "dead", 44]
first_name, last_name, *person_details = person
print(first_name, last_name, person_details)
