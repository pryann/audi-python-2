from os import path

file_path = path.join(path.dirname(__file__), "files", "text.txt")
# in other languages:
# file = open(file_path)
# print(file)
# file.close()

with open(file_path, "r+", encoding="utf-8") as f:
    # print(f.read())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    # set pointer to the beginning ot the file
    f.seek(0)
    # print(f.read())

    # for line in f:
    #     print("line", line, end="")

    lines = f.readlines()
    print(lines)

file_path = path.join(path.dirname(__file__), "files", "text2.txt")
with open(file=file_path, mode="a", encoding="UTF-8") as f:
    new_line = "\nfourth line"
    f.write(new_line)


file_path = path.join(path.dirname(__file__), "files", "text3.txt")
with open(file=file_path, mode="w", encoding="UTF-8") as f:
    content = "content"
    f.write(content)
