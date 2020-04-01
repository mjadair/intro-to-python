# *  ----- REDUCE  ------ *
# *  💻 Remember "fn" key + "f8" to run  your code

# * 🦉 Practice








# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

# ? Uncomment the following array

const numArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ? Define a const "total", assign its value to be the result of calling "reduce" on the numArray, returning the total sum of all numbers in the array.
# ? Log out "total" should return -> 55


const total = numArray.reduce((acc, curr) => {
  return acc + curr
}, 0)

console.log(total)


# ? Uncomment the following array

const nameArray = ['Jack', 'Abi', 'Charlotte', 'Guy']


# ? Define a const "nameString", assign its value to be the result of calling "reduce" on the nameArray, returning a string containing all the names in the array seperated by a space.
# ? Log out "nameString" should return -> 'Jack Abi Charlotte Guy'


const nameString = nameArray.reduce((str, curr) => {
  return str + `${curr} `
}, '')

console.log(nameString)


