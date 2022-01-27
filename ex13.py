from sys import argv
# read the WYSS section for how to run This
script, first, second, third, fourth = argv

word = input("Enter a Word:")
print(f"The word is {word}.")

print("The script is called:", script)
print("Your forst variable is:", first)
print("Your second variable is", second)
print("Your third variable is:", third)
print("The fourth variables is:", fourth)
