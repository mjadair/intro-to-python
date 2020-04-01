# Navigate to intro-to-python-complete folder and type python mixing-types.py to run

# *  ----- MIXING TYPES 🕺 ------ *

# * 🦉 Practice

# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

# ? Declare two varialbes, "numOne" and "numTwo", set their values to strings of number characters '10' and '5'

numOne = '10'
numTwo = '5'

# ? Declare a new variable called result, use the "+" operator to assign it a value and print it so it produces "105"

result = numOne + numTwo
print(result)

# ? What is the type of result currently? Print it using the built in "type()" function

print(type(result))

# ? Now re assign result to add the number 45 and print it. --> 150
# ? Print result in type again, what will it be now?

result = int(result) + 45
print(result)
print(type(result))
