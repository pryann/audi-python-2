user = {"name": "John Doe", "age": 33, "state": "dead"}
print(user["name"])

user["email"] = "johnthedeaddoe@gmail.com"
print(user)

user["age"] = 101
print(user)

user["hobbies"] = ["running", "agonisation"]
print(user)

print(user["hobbies"][0])

print("keys: ", user.keys())
print("keys: ", user.values())
print("keys: ", user.items())

user.pop("hobbies")
print(user)


for key, value in user.items():
    print(key, value)

cart_net_prices = {"VGA": 1000, "CPU": 500, "Monitor": 300}
cart_gross_prices = {k: v * 1.27 for k, v in cart_net_prices.items()}
print(cart_gross_prices)