#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = abs(number) % 10
print('Last digit of ' + str(number) + ' is ' + str(last_dig), end=' ')
if last_dig > 5:
    print('and is greater than 5')
elif last_dig == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')
