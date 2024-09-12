# yearly_salary = 101_000
# high_salary_criteria = 100_000

# # <, >, <=, >=, ==, !=
# if yearly_salary > high_salary_criteria:
#     print("High salary")
# else:
#     print("Low salary")


# grade = input("Please provide your grade: ")

# if grade == "1":
#     print("Elégtelen")
# elif grade == "2":
#     print("Elégséges")
# elif grade == "3":
#     print("Közepes")
# elif grade == "4":
#     print("Jó")
# elif grade == "5":
#     print("Jeles")
# else:
#     print("Ez nem egy osztályzat")


yearly_salaries = [
    100000,
    120000,
    130000,
    140000,
    150000,
    160000,
    170000,
    180000,
    190000,
    200000,
]

high_salary_criteria = 150_000
sum_high_salaries = 0
sum_low_salaries = 0

for salary in yearly_salaries:
    if salary >= high_salary_criteria:
        sum_high_salaries += salary
    else:
        sum_low_salaries += salary

print(sum_low_salaries, sum_high_salaries)
