# *  ----- ARRAY METHODS  ------ *
# ! Navigate to the directory and type `python list-methods.py` to run the file


# * 🦉 Practice


# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"


# ? Define a list called "foods", add a few strings of different food items, and print the list to the console

foods = ['pie', 'pizza', 'tacos']

print(foods)

# ? Using the list method "append", add another food item to the end of the array, and log it again.

foods.append('cheese')
print(foods)

# ? Use the list method "pop" to remove the first item of the array

foods.pop(0)
print(foods)

# ? Define a variable "joined". Assign its value to the foods list to a string of all the array items separated by  ','. Use the list method "join"

joined = ','.join(foods)
print(joined)