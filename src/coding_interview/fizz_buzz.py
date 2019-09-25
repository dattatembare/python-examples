"""
Fizz and Buzz refer to any number that's a multiple of 3 and 5 respectively.
In other words, if a number is divisible by 3, it is substituted with fizz; 
if a number is divisible by 5, it is substituted with buzz. 
If a number is simultaneously a multiple of 3 AND 5, the number is replaced with "fizz buzz.
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
