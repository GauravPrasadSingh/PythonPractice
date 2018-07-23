''''
Create a program that asks the user for a number and then prints out 
a list of all the divisors of that number.

There is an easy way to programmatically create lists of numbers in Python.
To create a list of numbers from 2 to 10, just use the following code:
x = range(2, 11)
'''

print(' We will find divisors for you')
num=int(input("Enter a number: "))
print("The divisor are :",end='')
divisors=[1]
for i in range(2,num//2+1):
    if num % i == 0:
        divisors.append(i)

divisors.append(num)
print(divisors)