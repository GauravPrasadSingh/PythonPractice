'''
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the 
elements of the list that are less than 5.
'''

list_1=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print('first loop approach')
for no in list_1:
    if no < 5:
        print(no)

#extras
'''
 Instead of printing the elements one by one, 
 make a new list that has all the elements 
 less than 5 from this list in it and print 
 out this new list.
Write this in one line of Python.
Ask the user for a number and 
return a list that contains only elements 
from the original list a that are smaller
 than that number given by the user.
'''
#filtering list in 1 line
list_new= [x for x in list_1 if x<5]
print('comprehension approach')
for no in list_new :
    print(no)

#another approach using lambda
list_new=list(filter(lambda x:x<5,list_1))
print('lambda approach')
for no in list_new :
    print(no)

print("Now we will show only those no less than no entered by user")
num=int(input("Enter a no"))
print('using comprehension approach')
for number in [x for x in list_1 if x<num]:
    print(number)