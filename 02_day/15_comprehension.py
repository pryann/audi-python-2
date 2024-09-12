numbers = []
for number in range(10):
    numbers.append(number)

print(numbers)

numbers = [number for number in range(10)]
print(numbers)

doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

matrix = [[i for i in range(5)] for j in range(5)]
print(matrix)
