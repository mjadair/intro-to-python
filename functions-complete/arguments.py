# Navigate to functions-complete folder and type python arguments.py to run

# * 🦉 Practice

# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

# ? Define a function "sayHello" that accepts a "name" parameter. It should return a string of 'Hello (the name)!'

def sayHello(name):
    return f'Hello {name}!'


# ? Call and print the result of the function twice, passing different "name" arguments.

print(sayHello('Jack'))
print(sayHello('Charlotte'))

# ? Define a function "add" that accepts two numbers, "a" and "b" as parameters. It should return the result of adding them together

def add(a, b):
    return a + b


# ? Call and print the result of the function a few times, passing different arguments.

print(add(10, 5))
print(add(2, 4))

# ? Define a function "shout" that accepts two strings as parameters. It should return the strings joined together in all uppercase eg 'hello', 'world' --> 'HELLOWORLD'

def shout(stringOne, stringTwo):
    return stringOne.upper() + stringTwo.upper()


# ? Call and print the result of the function a few times, passing different arguments.

print(shout('hello', 'world'))
print(shout('foo', 'bar'))

# ? Define a function "wordLength" that takes a string as a parameter, it should return a number of the length of that passed string

def wordLength(string):
    return len(string)

# ? Call and print the result of the function a few times, passing different arguments.

print(wordLength('hello'))
print(wordLength('foo'))


# ? Define a function "findCharacterIndex" that accepts two parameters, a string, and a number. The function should return the character in the passed string found at the passed index number. If the index to return is longer than the string, it should return the string 'Too long'

def findCharacterIndex(string, number):
    if number <= len(string):
        return string[number]
    return 'Too long'


# ? Call and print the result of the function a few times, passing different arguments.

print(findCharacterIndex('hello', 7))
print(findCharacterIndex('world', 3))
