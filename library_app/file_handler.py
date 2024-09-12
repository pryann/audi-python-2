def create_item_dict(item_row):
    id, title, author = item_row.rstrip().split(";")
    return {
        "id": int(id),
        "title": title,
        "author": author,
    }


def read_file(items_file):
    items = []
    # use csv module
    with open(items_file, mode="r", encoding="UTF-8") as f:
        for item in f:
            items.append(create_item_dict(item))
    return items


def write_file(items, items_file):
    with open(items_file, "w", encoding="UTF-8") as file:
        for item in items:
            item_line = ";".join(str(val) for val in item.values()) + "\n"
            # remove the last character
            file.write(item_line)
