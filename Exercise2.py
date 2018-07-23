'''
Ask the user for a number. 
Depending on whether the number is even or odd, 
print out an appropriate message to the user. 
'''
print("This app will tell whether a no is even or odd")
num=int(input("Enter a number"))
if num % 2 == 0:
    print("{0} is even.".format(num))
else:
    print("{0} is odd.".format(num))

#extras
'''
If the number is a multiple of 4,
 print out a different message.
Ask the user for two numbers: 
one number to check (call it num) 
and one number to divide by (check). 
If check divides evenly into num, 
tell that to the user. 
If not, print a different appropriate message.
'''      

if num % 4 == 0:
    print("{0} is a multiple of 4.".format(num))
print("We are going to check if one no divides second number.")
num1=int(input("Enter dividend no."))
num2=int(input("Enter divisor no."))
if num1 % num2 == 0:
    print("{1} is a factor of {0}".format(num1,num2))
else:
    print("remainder of {0}/{1} is {2}. ".format(num1,num2,num1%num2))        