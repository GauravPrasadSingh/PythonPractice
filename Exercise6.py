'''
Ask the user for a string and print out whether this string is a palindrome or not.
 (A palindrome is a string that reads the same forwards and backwards.)

 Some palindrome words
 deified, civic, radar, level, rotor, kayak, reviver, racecar, redder, madam, and refer.
 sentence- able was i ere i saw elba
'''

print("We are going to check palindrome")
string_1=input("Enter a word or sentence: ")
#approach 1 halfway checking
is_palindrome=True
for i in range(0,len(string_1)//2+1):
    if(string_1[i].lower() != string_1[len(string_1)-i-1].lower()):
        is_palindrome=False

if(is_palindrome):
    print(string_1+" is a palindrome")
else:
    print(string_1 +" is not a palindrome")


#approach 2 using loops i.e. forming a reversed word
def reverse_string(word):
    x=''
    for i in range(len(word)):
        x +=word[len(word)-1-i]
    return x

pstring=input('Enter a string')
if pstring == reverse_string(pstring):
    print("{0} is palindrome".format(pstring))
else:
    print("{0} is not palindrome".format(pstring))    
#approach 3 python
wrd=input("Please enter a word")
wrd=str(wrd)
'''
Python sequence slice addresses can be written as a[start:end:step] 
and any of start, stop or end can be dropped. 
 a[::-2] is every third element of the sequence.
 -negative step makes reverse
 however if you are using with negative start then negative step must be mentioned
'''
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")

#in one line could be written as
print(wrd)
print("{0} is a palindrome: {1} ".format(wrd,wrd[::] == wrd[::-1]))