yearly_salaries = [100000, 120000, 130000, 140000, 150000]

yearly_salaries.append(160000)
print(yearly_salaries)

yearly_salaries.extend([170000, 180000])
print(yearly_salaries)

yearly_salaries.insert(0, 90000)
print(yearly_salaries)

yearly_salaries[0] = 95000
print(yearly_salaries)

yearly_salaries[0:2] = [96000, 97000]
print(yearly_salaries)

yearly_salaries.remove(96000)
print(yearly_salaries)

yearly_salaries.pop(0)
print(yearly_salaries)

del yearly_salaries[0]
print(yearly_salaries)

# yearly_salaries.clear()
# print(yearly_salaries)

yearly_salaries.append(130000)

# count of value
print(yearly_salaries.count(130000))

# index
print(yearly_salaries.index(130000))

yearly_salaries.sort(reverse=True)
print(yearly_salaries)
