# *  ----- FOR LOOPS ------ *
# *  💻 Remember "fn" key + "f8" to run  your code

# * 🦉 Practice






# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

# ? Write a for loop that logs the numbers 0 - 10

for (let i = 0; i <= 10; i++) {
  console.log(i)
}

# ? Write a for loop that console logs the string 'Hello World' 10 times

for (let i = 0; i < 10; i++) {
  console.log('Hello World')  
}

# ? Write a for loop that console logs the numbers 50 to 88

for (let i = 50; i <= 88; i++) {
  console.log(i)
}

# ? BONUS - Declare a "let" with the label "result" and the value empty string.

# ? use a for loop and string concatenation to built the string '123456789' and log it to the console

let result = ''

for (let i = 1; i <= 9; i++) {
  result = result + i
}

console.log(result)


# *  ----- WHILE LOOPS ------ *
# *  💻 Remember "fn" key + "f8" to run  your code

# * 🦉 Practice










# ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

# ? Write a while loop that logs the numbers 0 - 10

let num = 0

while (num <= 10) {
  console.log(num)
  num++
}

# ? Write a while that console logs the string 'Hello World' 5 times

let current = 0

while (current < 5) {
  console.log('Hello World')
  current++
}


# ? BONUS - Write a while loop that will check if a random number is above or below 0.5, If it is the loop should print 'still running!' and the random number. When it has finished, it should log 'Stopped', and the randomNumber is stopped with. How many times will this log print?

let randomNumber = Math.random()

while (randomNumber > 0.5) {
  console.log('still running!')
  console.log(randomNumber)
  randomNumber = Math.random()
}

console.log('Stopped')
console.log(randomNumber)
