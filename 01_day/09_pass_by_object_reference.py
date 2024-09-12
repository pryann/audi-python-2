yearly_salaray_list = [120000, 100000, 72000, 50000]
yearly_salaray_list_copy = yearly_salaray_list

print("yearly_salaray_list", yearly_salaray_list)
print("yearly_salaray_list_copy", yearly_salaray_list_copy)
print("yearly_salaray_list memory address", id(yearly_salaray_list))
print("yearly_salaray_list_copy address", id(yearly_salaray_list_copy))

yearly_salaray_list.append(44000)
yearly_salaray_list_copy.append(55000)

print("yearly_salaray_list", yearly_salaray_list)
print("yearly_salaray_list_copy", yearly_salaray_list_copy)
print("yearly_salaray_list memory address", id(yearly_salaray_list))
print("yearly_salaray_list_copy address", id(yearly_salaray_list_copy))

yearly_salaray_list = [50000, 60000]
yslcc = yearly_salaray_list_copy.copy()
print("yearly_salaray_list", yearly_salaray_list)
print("yearly_salaray_list_copy", yearly_salaray_list_copy)
print("yearly_salaray_list memory address", id(yearly_salaray_list))
print("yearly_salaray_list_copy address", id(yearly_salaray_list_copy))
print("yearly_salaray_list_copy address", id(yslcc))
