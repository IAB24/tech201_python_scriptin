import os

# 1. Create a directory

# Directory
directory = "test_dir"

# Parent Directory
parent_dir = "C:/Users/Ilyas"

# Path
path = os.path.join(parent_dir, directory)

# # Create the DIR
# os.mkdir(path)
# print("Directory '% s' created" % directory)

# 2. Make a file in the new directory

filename = "textfile.text"
filepath = os.path.join(path, filename)

# Write to the new file
with open(os.path.join(path, filename), "w") as file1: # use open function to open file and write to it
    toFile = "Contents of my new file"
    file1.write(toFile)
print("File " + filename + "created in " + directory + "folder")