# Read a Python file (explicit version)
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# Read Python file (with manages closing the file)
with open("my_file.txt", mode = "r") as file:
    contents = file.read()
    print(contents)

# Write into the file
with open("my_file.txt", mode = "w") as file:
    contents = file.write("Hi, my name is Daniel and I'm overwriting this file!")
    
# Append text into the file
with open("my_file.txt", mode = "a") as file:
    contents = file.write("\nHi, it's me one more time!")
    
# If file does not exists, write mode creates it from scratch
with open("new_file.txt", mode = "w") as file:
    contents = file.write("Sup, new file!")