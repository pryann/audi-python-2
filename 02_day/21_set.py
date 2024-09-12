# unique elements
numbers = {1, 2, 3, 4, 5}
print(numbers)

# not subscriptable
# print(numbers[0])

numbers.add(6)
print(numbers)

numbers.remove(1)
print(numbers)

numbers.pop()
print(numbers)

# KeyError if not exsits
# numbers.remove(10)
print(numbers)

# not raise error if key not exists
numbers.discard(4)
print(numbers)


domains = ["audi", "bmw", "opel", "seat", "audi", "seat", "mazda"]
unique_domains = []
for domain in domains:
    if domain not in unique_domains:
        unique_domains.append(domain)
print(unique_domains)

unique_domains = list(set(domain))
