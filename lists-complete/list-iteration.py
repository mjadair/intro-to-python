// *  ----- ARRAY ITERATION ------ *
// *  💻 Remember "fn" key + "f8" to run  your code

// * 🦉 Practice









// ! ⚠️Remember to comment out your practice code before attempting below, "cmd" + "/"

// ? Define an array "students" and add some strings of names. Write a for loop that will log each item from the array in order.

const students = ['Jack', 'Charlotte', 'Abi', 'Guy', 'Mia']

for (let i = 0; i < students.length; i++) {
  console.log(students[i])
}

// ? Write a forEach statement that console logs each students name in order

students.forEach(student => {
  console.log(student)
})

// ? Write a forEach statment that console logs each students name, but with the letters of the name reversed.

students.forEach(student => {
  console.log(student.split('').reverse().join(''))
})