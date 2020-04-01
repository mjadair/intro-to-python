# *  ----- REDUCE  ------ *
# ! Navigate to the directory and type `python reduce.py` to run the file

# * 🦉 Practice



# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

# ? Uncomment the following list

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ? Define a variable "total", assign its value to be the result of calling "reduce" on the numList, returning the total sum of all numbers in the list.
# ? Print out "total" should return -> 55

import functools

total = (functools.reduce(lambda a,b : a+b,numList)) 

print(total)


# ? Uncomment the following list

nameList = ['Homer Simpson', 'Milhouse Vanhouten', 'Lionel Hutz', 'Chewbacca']


# ? Define a variable "nameString", assign its value to be the result of calling "reduce" on the nameList, returning a string containing all the names in the list seperated by a space.
# ? Log out "nameString" should return -> 'Jack Abi Charlotte Guy'


nameString = (functools.reduce(lambda a,b : a + ', ' + b,nameList)) 

print(nameString)


