from os import chdir, path

users_file = path.join(path.dirname(__file__), "files", "users.csv")


def create_user_dict(user_row):
    id, first_name, last_name, email = user_row.rstrip().split(";")
    return {
        "id": int(id),
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
    }


def get_file_data():
    users = []
    with open(users_file, mode="r", encoding="UTF-8") as f:
        for user in f:
            users.append(create_user_dict(user))
    return users


def append_user(user):
    with open(users_file, "a") as file:
        user_line = "\n" + ";".join(str(val) for val in user.values())
        file.write(user_line)


print(get_file_data())
