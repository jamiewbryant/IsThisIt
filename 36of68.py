'''
Author: Jamie W Bryant
Date: January 24, 2017
Python 38 of 68
'''
#1. Assign an integer to a variable
varI = 100

#2. Assign a string to a variable
varS = ('This is a string')

'''
3. Assign a float to a variable
Python 3 assigns float auto
'''
varF = float(2.3)

'''
#4. Use the print function and .format()
notation to print out the variable you assigned
'''
print('{0} {1}'.format(varI,varS))
print('I am {} years old'.format(varI))

'''
5. Use each of these operators
+, - , * , / , +=, ­= , %
'''
#Addition
5+5
#Subtraction
5-5
#Multiplication
5*5
#Division
5/5
#Add and Assign
varII = 200
varII += varF

#Equal or assign
varII = 200

#No remainder or a break
varR = varI / 24
varB = ('and start here')
varE = ('Start here, stop %s'%varB)

#6. Use of logical operators: and, or, not
if varI == 100 and varII == 200:
    print('Correct')
if varF < varII or varI:
    print('Correct Again')
if varI is not 200:
    print('I just cant help myself')

#7. Use of conditional statements: if, elif, else
varN = input('Enter your favorite number: ')

if varN.isdigit():
    print('Good one, but not my favorite')
elif not varN.isdigit():
    print('Come on not algebra')
else:
    print('Come on keep it simple')

#8. Use of a while loop
varL = 110
while (varL < 120):
    varL = varL + 1
    print(varL)
#9. Use of a for loop
for varF in range(0,3):
    print('Testing 3 times')

'''
10. Create a list and iterate through that list using
a for loop to print each item out on a new line
'''
a= ['Checking',1,2,3]
for varList in a:
    print(varList)

#11. Create a tuple and iterate through it using a for loop to print each item out on a new line
b = (1,2,3)
for varTuple in b:
    print(varTuple)

#12. Define a function that returns a string variable
varReturn=('Easy does it')
def varFunc(varReturn):
    return (varReturn + 'slick')
   
    
    
