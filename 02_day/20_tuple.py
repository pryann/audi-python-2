rgb_color = (120, 234, 55)
print(type(rgb_color))
print(rgb_color[0])

coordinates = (12.2324343,)
# vszeg rosszul választottad meg a típust
coordinates_list = list(coordinates)
coordinates_list.extend([34.2323232323, 1.123443434])
coordinates = tuple(coordinates_list)

print(coordinates)
coordinates += (11.12345, 44.4326)
print(coordinates)

tuple_2d = ((1, 2), (3, 4), [1, 2, 3, 4], None)
print(tuple_2d)
tuple_2d[2][0] = 0
print(tuple_2d)

numbers = (10, 20, 30, 40, 50)
# NEM COMPREHENSION, hanem genertaor expression + tuple conversion
square_numbers = tuple(i**2 for i in numbers)
print(square_numbers)
s