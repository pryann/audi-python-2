yearly_salaries = [
    100000,
    120000,
    130000,
    140000,
    150000,
]

print(yearly_salaries, type(yearly_salaries))
print(yearly_salaries[0])
print(yearly_salaries[1])
print(yearly_salaries[2])
print(yearly_salaries[0:3])

yearly_salaries[0] = 110099
print(yearly_salaries)

yearly_salaries_2 = [98_000, 99_000]
print(yearly_salaries + yearly_salaries_2)

print(yearly_salaries_2 * 2)

print(100_000 in yearly_salaries)


