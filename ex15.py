# Using argv module
# Lines 3 - 7 are used to get the file name
from sys import argv

script, filename = argv

txt = open(filename)

# Print the filename and its contents
print(f"Here's your file {filename}:")
print(txt.read())

# Close the file
txt.close()

# Using input() function
# Prompt for filename
print("Type the filename again:")
file_again = input("> ")

# Get the file
txt_again = open(file_again)

# Print file's contents
print(txt_again.read())

# Close the file
txt_again.close()
