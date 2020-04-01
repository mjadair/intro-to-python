# ? FizzBuzz
# ? Write a program that will log numbers from 1 - 101 in the console.
# ? Any number that is divisible by 3 should log "Fizz" instead of the number.
# ? Any number that is divisible by 5 should log "Buzz" instead of the number.
# ? Any number that is divisible by 3 and 5 should log "FizzBuzz" instead of the number.


for i in range(102):
    if i == 0:
        continue
    if i % 3 == 0 and i % 5 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)