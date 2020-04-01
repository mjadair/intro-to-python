# *  ----- ARRAY METHODS  ------ *
# *  💻 Remember "fn" key + "f8" to run  your code

# * 🦉 Practice









# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"


# ? Define an array called "foods", add a few strings of different food items, and log the array to the console

const foods = ['eggs', 'bacon', 'ham']

console.log(foods)

# ? Using the array method "push", add another food item to the end of the array, and log it again.

foods.push('cheese')
console.log(foods)

# ? Use the array method "slice" to remove the first item of the array

foods.splice(0, 1)
console.log(foods)

# ? Define a const "joined". Assign its value to the foods array to a string of all the array items joined together. Use the array method "join"

const joined = foods.join('')
console.log(joined)