def generate_new_id(items):
    # if items is empty, set new id to 1
    return max(item["id"] for item in items) + 1


def list_items(items):
    return items


def find_item(id, items):
    for item in items:
        if item["id"] == id:
            return item


def create_item(item, items):
    base_item = {"id": generate_new_id(items)}
    base_item.update(item)
    items.append(base_item)
    return items[-1]


def remove_item(id, items):
    item = find_item(id, items)
    if item is not None:
        items.remove(item)


def update_item(id, updated_item, items):
    item = find_item(id, items)
    if item is not None:
        index = items.index(item)
        items[index].update(updated_item)
        return items[index]
