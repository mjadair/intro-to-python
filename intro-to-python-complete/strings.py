# *  ----- STRINGS  ------ *
# Navigate to intro-to-python-complete folder and type python strings.py to run

# * 🦉 Practice

# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

# ? Define a string as a variable, log that string and its length to the console

myName = 'Nick'

print(myName)

print(len(myName))

# ? Using the "+" syntax and the string defined above, print the string "The word (myString) is (myStringLength) characters long"

print('The word ' + myName + ' is ' + str(len(myName)) + ' characters long')

# ? Try again using the string interpolation syntax.

print(f'The word {myName} is {len(myName)} characters long')

# * ---- STRING METHODS 🧪 ---- *

# * 🦉 Practice

# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

# ? Declare the string value 'python' as a variable all lowercase, using string methods do the following:

string = 'python'

# ? Print the string to the console all in uppercase -> 'PYTHON'

print(string.upper())

# ? Print it title cased -> 'Python'

print(string.title())

# ? Bonus, print it like this -> 'Python 😎'

print(f'{string.title()} 😎')