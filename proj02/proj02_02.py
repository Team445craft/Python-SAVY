# Name: Trey Owen
# Date: July 2017

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
print ""
print "Welcome to Fibonaci Sequence Generator. Last updated July 2017.\nBy Trey Owen."
print ""
enter = raw_input("Press ENTER")
print ""

# Generator
numbers = 0
loop = True
# numbers

prev = 0
next = 1

numbers = int(raw_input("To generate numbers, enter the amount of numbers you need (1+): "))
while loop == True:
    if numbers > 1:

        while loop == True:
            print prev + next, ","
            next2 = (next + next)
            print next2
            prev = 2
            next = 3
            print prev + next,","
    else:
        print "[Error] That was done incorrectly."
