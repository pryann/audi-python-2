def greeting(name):
    print(f"Helloooo {name}")
    return


print(type(greeting("Gizi")))
greeting("Marci")
greeting("Jónás")

# print(dir(__builtins__))


def even_or_odd(number):
    return "even" if number % 2 == 0 else "odd"


print(even_or_odd(10))
print(even_or_odd(9))


def calculate_gross_price(net_price, vat_percent=27):
    return net_price * (1 + vat_percent / 100)


print(calculate_gross_price(10000))
print(calculate_gross_price(1000, 5))
print(calculate_gross_price(1000))
print(calculate_gross_price(vat_percent=5, net_price=50000))


def add_item_to_basket(item, basket=None):
    if not basket:
        basket = []
    basket.append(item)
    return basket


print(add_item_to_basket("VGA"))
print(add_item_to_basket("VGA"))
print(add_item_to_basket("VGA"))
