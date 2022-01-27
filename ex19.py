def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

# Numbers as inputs
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Variables as inputs
print("or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Numbers can be added
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Variable and Numbers can be joined
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)

# Variables can be added
print("We can join two varibales too:")
x = 97
y = 89
cheese_and_crackers(amount_of_cheese + x, amount_of_crackers + y)
