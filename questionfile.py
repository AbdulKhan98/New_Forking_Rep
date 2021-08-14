#In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:

def animal_legs(animals = ()):
	count_animal = int(()legs)

animals_legs(chickens = 2 legs)
animals_legs(cows = 4 legs)
animals_legs(dogs = 4 legs)

#The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a script or function that returns the total number of legs of all the animals.

#Example 1
#animals(2, 3, 5) ➞ 36

#Example 2
#input(1, 2, 3) ➞ 22

#Example 3
#How many Chickens? 5
#How many Cows? 2
#How many Dogs? 8
#50 legs

#Create a python script to solve this problem.

chicken = int(input("Enter number of chickens: "))
cow = int(input("Enter number of cows: "))
dog = int(input("Enter number of dogs: "))

def count_legs():
    chicken_legs = chicken * 2
    cow_legs = cow * 4
    dog_legs = dog * 4
    legs_sum = chicken_legs + cow_legs + dog_legs
    return legs_sum


print("Number of legs is {}".format(count_legs()))

