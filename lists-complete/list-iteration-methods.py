# *  ----- FILTERING ARRAYS ------ *
# ! Navigate to the directory and type `python list-iteration-methods.py` to run the file

# * 🦉 Practice


# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"


# ? Uncomment the followng list

fruits = ['apple', 'pear', 'strawberry', 'kiwi', 'passion fruit', 'mango']


# ? Define a variable "smallFruits" and assign it value of the fruits list, filtered to only contain fruits with 4 charaters or less
# ? Print the "smallFruits" array and expect to see -> ['pear', 'kiwi']

smallFruits = list(filter(lambda x: len(x)<= 4, fruits))

print(smallFruits)

#OR

smallFruitsAlternative = [x for x in fruits if len(x) <= 4]

print(smallFruitsAlternative)

# ? Define a const "bigFruits" and assign it value of the fruits array, filtered to only contain fruits with more than 6 characters
# ? Log the "bigFruits" array and expect to see -> ['stawberry', 'passion fruit']

bigFruits = list(filter(lambda x: len(x)>= 6, fruits))

print(bigFruits)


bigFruitsAlternative = [x for x in fruits if len(x) >= 6]

print(bigFruitsAlternative)


# ? Define a const "mediumFruits" and assign it value of the fruits array, filtered to only contain fruits with more than 4 characters but less than or equal to 6 characters
# ? Log the "mediumFruits" array and expect to see -> ['apple', 'mango']

mediumFruits = list(filter(lambda fruit: len(fruit)> 4 and len(fruit) <= 6 , fruits))
 
print(mediumFruits)

mediumFruitsAlternative = [fruit for fruit in fruits if len(fruit) > 4 and len(fruit) <= 6]

print(mediumFruitsAlternative)

# ? Print the original "fruits" array. What has happened to it?


print(fruits)


# *  ----- MAPPING ARRAYS ------ *
# ! Remember to type `python list-iteration-methods.py` in terminal to run the file

# * 🦉 Practice

# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

# ? Uncomment the followng list

cities = ['London', 'New York', 'Paris', 'Tokyo', 'Los Angeles']

# ? Define a variable "cityLengths" and assign it the value of the cities list, mapped into an array indicating the length of each city string
# ? Log the "cityLengths" list and expect to see -> [6, 8, 5, 5, 11]


cityLengths = list(map(lambda city: len(city), cities))

print(cityLengths)

altCityLengths = [len(city) for city in cities]

print(altCityLengths)


# ? Define a variable "cityShouts" and and assign it the value of the cities list, mapped into an array where all the strings have been transformed to uppercase with a '!' on the end
# ? Print the "cityShouts" list and expect to see ->  'LONDON!', 'NEW YORK!', 'PARIS!', 'TOKYO!', 'LOS ANGELES!' ]

# const cityShouts = cities.map(city => {
#   return city.toUpperCase() + '!'
# })


cityShouts = [city.upper() + '!' for city in cities]

print(cityShouts)


# ? Log the original "cities array. What has happened to it?


print(cities)