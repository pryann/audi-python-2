# # minimum kiváalsztás - mi van ha nulla elemű, vizsgálni kellene
# def get_minimum_value(numbers):
#     # if len(numbers) == 0:
#     #     return None
#     min_value = numbers[0]
#     for i in range(1, len(numbers)):
#         if numbers[i] < min_value:
#             min_value = numbers[i]
#     return min_value


# # minimum kiváalsztás, ha nula elemű akkor a +inf lesz a legkisebb elem
# # vizsgálni kllene itt is hggy nulla elemű e

# # def get_minimum_value(numbers):
# #     min_value = float("inf")
# #     for number in numbers:
# #         if number < min_value:
# #             min_value = number
# #     return min_value

# print(get_minimum_value([1, 2, 3, 4, 5]))
# print(min([1, 2, 3, 4, 5]))


# # maximum kiválasztás
# def get_maximum_value(numbers):
#     max_value = numbers[0]
#     for i in range(1, len(numbers)):
#         if numbers[i] > max_value:
#             max_value = numbers[i]
#     return max_value


# print(get_maximum_value([1, 2, 3, 4, 5]))
# print(max([1, 2, 3, 4, 5]))


# # összegzés
# def summa(numbers):
#     sum_values = 0
#     for number in numbers:
#         sum_values += number
#     return sum_values


# # átlag
# def average(numbers):
#     return summa(numbers) / len(numbers)


# print(summa([1, 2, 3, 4, 5]))
# print(sum([1, 2, 3, 4, 5]))

# print(average([1, 2, 3, 4, 5]))


# # megszámlálás
# def count_value(numbers, value):
#     counter = 0
#     for number in numbers:
#         if number == value:
#             counter += 1
#     return counter


# print(count_value([1, 2, 3, 4, 5, 2, 2, 3], 2))
# print(
#     [
#         1,
#         2,
#         3,
#         4,
#         5,
#         2,
#         2,
#         3,
#     ].count(2)
# )


# # kiválasztás
# def get_index(numbers, value):
#     for i in range(len(numbers)):
#         if numbers[i] == value:
#             return i


# print(get_index([1, 2, 3, 4, 5], 2))
# print([1, 2, 3, 4, 5].index(2))


# # eldöntés
# def is_contains(numbers, value):
#     for number in numbers:
#         if number == value:
#             return True
#     return False


# print(is_contains([1, 2, 3, 4, 5], 2))
# print("2" in [1, 2, 3, 4, 5])


# # lineáris keresés
# def linear_search(numbers, value):
#     for i in range(len(numbers)):
#         if numbers[i] == value:
#             return i


# # buble sort
# def bubble_sort(values):
#     for i in range(len(values)):
#         for j in range(len(values) - i - 1):
#             if values[j] > values[j + 1]:
#                 values[j], values[j + 1] = values[j + 1], values[j]
#     return values


def advanced_bubble_sort(values):
    for i in range(len(values)):
        swapped = False
        for j in range(len(values) - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
        if not swapped:
            return values


print(advanced_bubble_sort([1, 2, 3, 4, 6, 5]))
my_list = [1, 2, 3, 4, 6, 5]
my_list.sort()
print(my_list)
