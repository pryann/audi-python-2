users = [
    {
        "id": 1,
        "first_name": "Risa",
        "last_name": "Groundwator",
        "email": "rgroundwator0@netscape.com",
    },
    {
        "id": 2,
        "first_name": "Guillemette",
        "last_name": "Ezele",
        "email": "gezele1@vistaprint.com",
    },
    {
        "id": 3,
        "first_name": "Yul",
        "last_name": "Pritchard",
        "email": "ypritchard2@cbslocal.com",
    },
    {
        "id": 4,
        "first_name": "Verile",
        "last_name": "Dealey",
        "email": "vdealey3@jalbum.net",
    },
    {
        "id": 5,
        "first_name": "Dag",
        "last_name": "Batterton",
        "email": "dbatterton4@un.org",
    },
]


def list_users():
    return users


def find_user(id):
    for user in users:
        if user["id"] == id:
            return user


def create_user(user):
    users.append(user)
    return users[-1]


def remove_user(id):
    user = find_user(id)
    if user is not None:
        users.remove(user)


def update_user(id, updated_user):
    user = find_user(id)
    if user is not None:
        index = users.index(user)
        users[index].update(updated_user)
        return users[index]


# print(find_user(2))
# create_user(
#     {"id": 6, "first_name": "New", "last_name": "User", "email": "newuser@gmail.com"}
# )
remove_user(1)
update_user(2, {"first_name": "Johnny"})
print(users)
