# *  ----- ARRAYS  ------ *
# ! Navigate to the directory and type `python lists.py` to run the file

# * 🦉 Practice

# ! ⚠️Comment out your practice code before attempting below, "cmd" + "/"


# ? Define a variable called students that is a list. Add the name of four of your classmates as strings.

students = ['Nick', 'Guy', 'Michael', 'Jonny']

# ? Access the first name in the array and log it to the console.

print(students[0])

# ? Access the third name in the array and log it to the console.

print(students[2])

# ? Reassign the last item in the array to be a different name and log it

students[3] = 'Little Fiddy Finkerstein'
print(students[3])

# ? Log the length of the array 

print(len(students))

# ? Use the length property to log the final name in the array

print(students[len(students) - 1])