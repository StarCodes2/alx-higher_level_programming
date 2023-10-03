#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = number % 10
last = 0

if (number < 0) and (temp != 0):
    last = int(temp * (-1))
else:
    last = temp

print('Last digit of {:d} is {:d}'.format(number, last), end=' ')

if last > 5:
    print('and is greater than 5')
elif (last < 6) and (last != 0):
    print('and is less than 6 and not 0')
elif last == 0:
    print('and is 0')
