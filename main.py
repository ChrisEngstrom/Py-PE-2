#!/usr/bin/env python3

fibValueLimit = 4000000
n = 0
nMinusOne = 1
nMinusTwo = 0
sumOfEvenFibs = 0

def Fibonacci(limit):
    global n
    global nMinusOne
    global nMinusTwo
    global sumOfEvenFibs

    n = nMinusOne + nMinusTwo

    if (n > limit):
        return sumOfEvenFibs
    else:
        if (n % 2 == 0):
            sumOfEvenFibs += n
        
        nMinusTwo = nMinusOne
        nMinusOne = n

        return Fibonacci(limit)

print('Sum of even Fibonacci numbers less than ' + str(fibValueLimit) + ': ' + str(Fibonacci(fibValueLimit)))
