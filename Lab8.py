import math
# User input the first name in lowercase letter.
first_name=input("Enter First Name : ")
  
# User input the last name in uppercase letter.
last_name=input("Enter Last Name : ")
  
# First name converted to uppercase Letter
first_name=first_name.upper()
  
# Last name converted to lowercase Letter
last_name=last_name.lower()
  
# Print statement as like #8 says.
print('"Hello,',first_name,last_name,'"',)
print()
print()
print('"Start by doing what',"'","s necessary; then do what","'",'s possible; and suddenly you are doing the impossible - Francis of Assisi"',sep='')

# 2 numbers as decimal variables
num1 = 3.3
num2 = 10.7

# Stores operations
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

# Print out results from each operation
print('{} plus {} equals {}'.format(num1, num2, add))
print('{} minus {} equals {}'. format(num1, num2, sub))
print('{} multiplied by {} equals {}'.format(num1, num2, mul))
print('{} divided by {} equals {}'.format(num1, num2, div))

# Sets squareroot variable and prints it
sq_root = math.sqrt(mul)
print('The square root of {} equals {}'.format(mul,sq_root))

# Created string variable for month and numeric variable for the day
month = 'November'
day = 20

# Print out what day and month it is
print('\t\tToday is', day, ' of the month of ', month )