'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements 
that are common between the lists (without duplicates).
 Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python 
(don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#approach1 - use sets
set_a=set(a)
set_b=set(b)
print('approach 1')
print("Common elements between {0} and {1} \n are {2}"
.format(a,b,set_a.intersection(set_b)))


print("Common elements between {0} and {1} \n are {2}"
.format(a,b,set_a & set_b))
#can also be written as list(set(a)&set(b)) more concisely

#approach2 - iterate through lists
c=[]
for no in a:
    if no in b and no not in c:
        c.append(no)
print('approach 2')
print(c)

#approach 3- in one line using comprehension list predicate form
print('approach 3')
print([i for i in b if i in a])

#generate random list
import random
c = random.sample(range(1, 50),35)
d = random.sample(range(25, 35), 10)
#finding common elements
print([y for y in d if y in c])
