from os import getcwd, path

print("getcwd():", getcwd())
print("__file__:", __file__)
print("abspath:", path.abspath(__file__))
print("dirname:", path.dirname(__file__))
print("basename:", path.basename(__file__))

# use path concetanation, relative path, the root is THIS file
print(path.join(path.dirname(__file__), "files", "text.txt"))
# on the top of the file, change dir
# chdir()
