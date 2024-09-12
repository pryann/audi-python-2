global_variable = "global"

print(global_variable)


def log_global_value():
    print(global_variable)


log_global_value()


def local_scope():
    local_variable = "local"
    print(local_variable)


local_scope()
# local_variable

name = "Gergely"


def scope_test():
    global name
    name = "Józsi"
    print(name)


scope_test()
print(name)


def add_item_to_basket(item, basket):
    basket.append(item)


cart = []
add_item_to_basket("VGA", cart)
add_item_to_basket("Processor", cart)
add_item_to_basket("Monitor", cart)
print(cart)


def gcd_loop(a, b):
    while b:
        # temp = a
        # a = b
        # b = temp % b
        a, b = b, a % b
    return a


def gcd_rec(a, b):
    return a if b == 0 else gcd_rec(b, a % b)


print(gcd_loop(30, 330))
print(gcd_rec(30, 330))
empty_string = ""
