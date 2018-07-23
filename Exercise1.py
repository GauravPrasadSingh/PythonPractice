'''
Create a program that asks the user 
to enter their name and their age. 
Print out a message addressed to them 
that tells them the year that they will turn 100 years old.
'''
from datetime import datetime
name=input('Enter your name: ')
age=int(input('Enter your age: '))
year_hundred =datetime.now().year+(100-age)
print("Hello {0}. You will turn 100 in year {1}.".
format(name,year_hundred))
#printing above message n number of times
#where n is passed by user
n=int(input('''Enter no of times you want to print
above message''')) 
print("Hello {0}. You will turn 100 in year {1}.\n".
format(name,year_hundred)*n)