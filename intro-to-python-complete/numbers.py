# *  ----- NUMBERS 🧮 ------

import math
import random

# Navigate to intro-to-python-complete folder and type python numbers.py to run


# * 🦉 Practice


# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

# ? Define a variable with the label "num" and assign the value 10

num = 10

# ? Define a variable "result", assign its value to our "num" + 50, and print it --> 60

result = num + 50
print(result)

# ? reassign "result", to be the value of itself divided by 2, print it out --> 30

result = result / 2
print(result)

# ? reassign "result" again, to be the value of itself minus 9 --> 21

result = result - 9
print(result)

# ? reassign "result" again, to be value of itself divided by 7 --> 3

result = result / 7
print(result)

# ? Print the float 3.3 to the nearest number

print(round(3.3))

# ? Print the float 10.8 rounded to 10

print(math.floor(10.8))

# ? Print the float 4.2 round to 5

print(math.ceil(4.2))

# ? Print a random number between 1 and 10

print(random.randint(1,10))
