// *  ----- FILTERING ARRAYS ------ *
// *  💻 Remember "fn" key + "f8" to run  your code

// * 🦉 Practice









// ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"


// ? Uncomment the followng array

const fruits = ['apple', 'pear', 'strawberry', 'kiwi', 'passion fruit', 'mango']


// ? Define a const "smallFruits" and assign it value of the fruits array, filtered to only contain fruits with 4 charaters or less
// ? Log the "smallFruits" array and expect to see -> ['pear', 'kiwi']

const smallFruits = fruits.filter(fruit => {
  return fruit.length <= 4
})

console.log(smallFruits)

// ? Define a const "bigFruits" and assign it value of the fruits array, filtered to only contain fruits with more than 6 characters
// ? Log the "bigFruits" array and expect to see -> ['stawberry', 'passion fruit']

const bigFruits = fruits.filter(fruit => {
  return fruit.length > 6
})

console.log(bigFruits)

// ? Define a const "mediumFruits" and assign it value of the fruits array, filtered to only contain fruits with more than 4 characters but less than or equal to 6 characters
// ? Log the "mediumFruits" array and expect to see -> ['apple', 'mango']

const mediumFruits = fruits.filter(fruit => {
  return fruit.length > 4 && fruit.length <= 6
})

console.log(mediumFruits)

// ? Log the original "fruits" array. What has happened to it?

console.log(fruits)


// *  ----- MAPPING ARRAYS ------ *
// *  💻 Remember "fn" key + "f8" to run  your code

// * 🦉 Practice











// ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

// ? Uncomment the followng array

const cities = ['London', 'New York', 'Paris', 'Tokyo', 'Los Angeles']

// ? Define a const "cityLengths" and assign it the value of the cities array, mapped into an array indicating the length of each city string
// ? Log the "cityLengths" array and expect to see -> [6, 8, 5, 5, 11]

const cityLengths = cities.map(city => {
  return city.length
})

console.log(cityLengths)


// ? Define a const "cityShouts" and and assign it the value of the cities array, mapped into an array where all the strings have been transformed to uppercase with a '!' on the end
// ? Log the "cityShouts" array and expect to see ->  'LONDON!', 'NEW YORK!', 'PARIS!', 'TOKYO!', 'LOS ANGELES!' ]

const cityShouts = cities.map(city => {
  return city.toUpperCase() + '!'
})

console.log(cityShouts)

// ? Log the original "cities array. What has happened to it?


console.log(cities)