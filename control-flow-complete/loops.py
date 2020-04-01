# *  ----- FOR LOOPS ------ *
# ! Navigate to the directory and type `python loops.py` to run the file

# * 🦉 Practice


# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

# ? Write a for loop that logs the numbers 0 - 10

for i in range(11):
  print(i)


# ? Write a for loop that console logs the string 'Hello World' 10 times

for i in range(10):
    print('Hello World')

# ? Write a for loop that console logs the numbers 50 to 88

for i in range(89):
    if i < 50:
        continue
    print(i)

# ? BONUS - Declare a variable called "result" and the value of an empty string.

# ? use a for loop and string concatenation to built the string '123456789' and print to the console

result = ''

for i in range(10):
    result = result + str(i)

print(result)


# *  ----- WHILE LOOPS ------ *
# ! Remember, run`python loops.py` to run the file

# * 🦉 Practice


# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

# ? Write a while loop that logs the numbers 0 - 10

num = 0

while num <= 10:
  print(num)
  num += 1


# ? Write a while that console logs the string 'Hello World' 5 times

current = 0

while (current < 5):
  print('Hello World')
  current += 1


# ? BONUS - Write a while loop that will check if a random number is above or below 0.5, If it is the loop should print 'still running!' and the random number. When it has finished, it should log 'Stopped', and the randomNumber is stopped with. How many times will this log print?

import random

randomNumber = (random.random())

while randomNumber > 0.5:
  print('still running!')
  print(randomNumber)
  randomNumber = (random.random())
print('Stopped')
print(randomNumber)
