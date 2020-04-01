// *  ----- MIXING TYPES 🕺 ------ *
// *  💻 Remember "fn" key + "f8" to run  your code

// * 🦉 Practice





// ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

// ? Declare two "consts", "numOne" and "numTwo", set their values to strings of number characters '10' and '5'

const numOne = '10'
const numTwo = '5'

// ? Declare a new variable with "let" called result, use the "+" operator to assign it a value and log it so it produces "105"

let result = numOne + numTwo
console.log(result)

// ? What is the type of result currently? Log it using the built in "typeof()" function

console.log(typeof (result))

// ? Now re assign result to add the number 45 and log it. --> 150
// ? Log result in typeof again, what will it be now?

result = parseInt(result) + 45
console.log(result)
console.log(typeof (result))

