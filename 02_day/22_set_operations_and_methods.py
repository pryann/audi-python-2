x1 = {"a", "b", "c"}
x2 = {"b", "c", "d"}

print(x1.union(x2))
print(x1.intersection(x2))
print(x1.difference(x2))
print(x1.symmetric_difference(x2))
print(x1.issubset({"a", "b", "c", "d"}))
print(x1.issuperset({"a", "b"}))
print(x1.isdisjoint(x2))

x = {1, 2, 3}
x |= {5, 6, 7}
print(x)

x1 = {"a", "b", "c"}
x2 = {"b", "c", "d"}
print("union", x1 | x2)
print("intersection", x1 & x2)
print("diff", x1 - x2)
print("sim diff", x1 ^ x2)
print("issubset", x1 <= {"a", "b", "c", "d"})
print("issuperset", x1 >= {"b", "c"})
