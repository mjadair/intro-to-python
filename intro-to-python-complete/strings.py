// *  ----- STRINGS  ------ *
// *  💻 Remember "fn" key + "f8" to run  your code

// * 🦉 Practice






// ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

// ? Define a string as a const, log that string and its length to the console

const myName = 'Jack'

console.log(myName)

console.log(myName.length)

// ? Using the "+" syntax and the string defined above, console.log the string "The word (myString) is (myStringLength) characters long"

console.log('The word ' + myName + ' is ' + myName.length + ' characters long')

// ? Try again using the "``" syntax.

console.log(`The word ${myName} is ${myName.length} characters long`)

// * ---- STRING METHODS 🧪 ---- * 
// *  💻 Remember "fn" key + "f8" to run  your code


// * 🦉 Practice






// ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"


// ? Declare the string value 'javascript' as a const all lowercase, using string methods do the following:

const string = 'javascript'

// ? Log the string to the console all in uppercase -> 'JAVASCRIPT'

console.log(string.toUpperCase())

// ? Log it title cased -> 'Javascript'

console.log(`${string.charAt(0).toUpperCase()}${string.slice(1)}`)

// ? Bonus, log it like this -> 'JavaScript 😎'

console.log(`${string.charAt(0).toUpperCase()}${string.slice(1, 4)}${string.charAt(4).toUpperCase()}${string.slice(5)} 😎`)