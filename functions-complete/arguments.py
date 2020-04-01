// *  ----- ARGUMENTS & PARAMETERS  ------ *
// *  💻 Remember "fn" key + "f8" to run  your code

// * 🦉 Practice








// ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

// ? Define a function "sayHello" that accepts a "name" parameter. It should return a string of 'Hello (the name)!'

function sayHello(name) {
  return `Hello ${name}!`
}

// ? Call and log the result of the function twice, passing different "name" arguments.

console.log(sayHello('Jack'))
console.log(sayHello('Charlotte'))

// ? Define a function "add" that accepts two numbers, "a" and "b" as parameters. It should return the result of adding them together

function add(a, b) {
  return a + b
}

// ? Call and log the result of the function a few times, passing different arguments.

console.log(add(10, 5))
console.log(add(2, 4))

// ? Define a function "shout" that accepts two strings as parameters. It should return the strings joined together in all uppercase eg 'hello', 'world' --> 'HELLOWORLD'

function shout(stringOne, stringTwo) {
  return stringOne.toUpperCase() + stringTwo.toUpperCase() 
}

// ? Call and log the result of the function a few times, passing different arguments.

console.log(shout('hello', 'world'))
console.log(shout('foo', 'bar'))