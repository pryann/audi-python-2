from os import mkdir, path, chdir, rename, rmdir

# dir_name = path.join(path.dirname(__file__), "directory")
# mkdir(dir_name)

chdir(path.dirname(__file__))
# mkdir("directory")
# rename("directory", "newdirectory")

rmdir("newdirectory")

# you can use shutils too for folder operations
