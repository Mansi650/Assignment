#String Exercises
#1. Write a Python program to count the number of characters (character frequency) in a string

def char_frequency(s):
    dict={}
    for n in s:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict
print(char_frequency('google.com'))

Output:-{'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}


#2
#Sample String : 'restart'
#Expected Result : 'resta$t'

def change_char(str1):
    char=str1[0]
    str1=str1.replace(char,'$')
    str1=char+str1[1:]

    return str1
print(change_char('restart'))

Output:-resta$t


#3. Write a Python function that takes a list of words and returns the length of the longest one

def longest_words(w):
    word_len=[]
    for n in w:
        word_len.append((len(n),n))
    word_len.sort()
    return word_len[-1][0]

print(longest_words(["Mary","Roshan","Krishnakant","Seema"]))

Output:-11



#5. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

def to_uppercase(str):
    num_upper=0
    for char in str[:4]:
        if char.upper()==char:
            num_upper+=1
    if num_upper>=2:
        return str.upper()
    return str

print(to_uppercase("python"))
print(to_uppercase("PyThon"))

Output:-python
        PYTHON


#6. Write a Python program to count and display the vowels of a given text

str="fashion"
count=0
for i in str:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
      count+=1
      print(i)
print("No. of vowels are:", count)

Output:-
a
i
o
No. of vowels are: 3


#Lists Exercises

#1. Write a Python program to check a list is empty or not

l=[1,3.3]
if l==[]:
    print("list is empty")
else:
    print("list is not empty")

Output:-list is not empty


#2. Write a Python program to remove duplicates from a list

a=[10,20,30,40,50,10,20,30,40,80,60]

d=set()
unique=[]
for x in a:
    if x not in d:
        unique.append(x)
        d.add(x)
        
print(d) 

Output:-{40, 10, 80, 50, 20, 60, 30}


#3. Write a Python function that takes two lists and returns True if they have at least one common member

def common_member(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
                return result
            
print(common_member([1,2,3,4,5],[2,5,6,8,9,6,7]))  
print(common_member([1,2,3,4],[5,6,7,8,9]))

Output:-True
        None


#4. Write a Python program to get the difference between the two lists

l1=[2,4,6,8,10]
l2=[1,2,3,4,5]
print(list(set(l1)-set(l2)))

Output:-[8, 10, 6]


#5. Write a Python program to find the second smallest number in a list

a=[]
n=int(input("Enter no. of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Second smallest no. is:",a[1])

Output:-Enter no. of elements:3
        Enter element:34
        Enter element:12
        Enter element:24
        Second smallest no. is: 24


#6. Write a Python program to find the second largest number in a list

a=[]
n=int(input("Enter no. of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Second largest no. is :",a[n-2])

Output:-Enter no. of elements:4
        Enter element:45
        Enter element:34
        Enter element:25
        Enter element:22
        Second largest no. is : 34


#7. Write a Python program to get the frequency of the elements in a list

import collections
l1=[10,20,30,40,20,10,30,40,10,20,30,40]
print("Original list:",l1)
ctr=collections.Counter(l1)
print("Frequency of elements in the list:",ctr)

Output:-Original list: [10, 20, 30, 40, 20, 10, 30, 40, 10, 20, 30, 40]
        Frequency of elements in the list: Counter({10: 3, 20: 3, 30: 3, 40: 3})


#8. Write a Python program to convert a list of multiple integers into a single integer
#Sample list: [11, 33, 50]
#Expected Output: 113350

l1=[23,67,78,45]
for i in l1:
    print(i,end="")

Output:-23677845


#Dictionary Exercises

#1. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
#Sample Dictionary ( n = 5) :
#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)

Output:-Enter a number:3
        {1: 1, 2: 4, 3: 9}


#2. Write a Python program to combine two dictionary adding values for common keys
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

from collections import Counter
d1={"a":12, "b":34, "c":35, "d":30}
d2={"a":20, "c":20, "f":20}
dict=Counter(d1)+Counter(d2)
print(dict)

Output:-Counter({'c': 55, 'b': 34, 'a': 32, 'd': 30, 'f': 20})


#7. Write a Python program to convert a list into a nested dictionary of keys

l=[1,2,3,4]
d=current={}
for i in l:
    current[i]={}
    current=current[i]
print(d)    

Output:-{1: {2: {3: {4: {}}}}}



#Tuple Exercises

#1. Write a Python program to create a tuple with different data types.

t1=("Mansi", 23, 26.45)
print(t1)

Output:-('Mansi', 23, 26.45)


#2. Write a Python program to add an item in a tuple

t1=(10,20,30,40)
print(t1)

t1=t1+(50,)
print(t1)

l=list(t1)
l.append(60)
t1=tuple(l)
print(t1)

Output:-(10, 20, 30, 40)
        (10, 20, 30, 40, 50)
        (10, 20, 30, 40, 50, 60)


#3. Write a Python program to convert a tuple to a string

def convertTuple(tup):
    str=''.join(tup)
    return str

tuple=('g','o','o','g','l','e')
str=convertTuple(tuple)
print(str)

Output:-google


#5. Write a Python program to find the length of a tuple

t=('I','n','d','i','a')
print(t)
print(len(t))

Output:-('I', 'n', 'd', 'i', 'a')
        5


#Conditional statements and loops Exercises
 
#1. Write a Python program to count the number of even and odd numbers from a series of numbers

numbers=(1,2,3,4,5,6,7,8,9)
count_odd=0
count_even=0
for x in numbers:
    if not x%2:
        count_even+=1
    else:
        count_odd+=1
print("Number of even numbers:",count_even) 
print("Number of odd numbers:",count_odd)

Output:-Number of even numbers: 4
        Number of odd numbers: 5


#2. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6

for x in range(6):
    if (x==3 or x==6):
        continue
    print(x,end=' ')
print("\n")    

Output:-0 1 2 4 5


#3. Write a Python program to get the Fibonacci series between 0 to 50.

x,y=0,1

while y<50:
    print(y)
    x,y=y,x+y

Output:-1
        1
        2
        3
        5
        8
        13
        21
        34



#5. Write a Python program to create the multiplication table (from 1 to 10) of a number.

n=int(input("Enter a number:"))
for i in range(1,11):
    print(n,'x',i,'=',n*i)

Output:-Enter a number:4
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40



#Functions Exercises

#1. Write a Python function to find the Max of three numbers.

def maximum(a,b,c):
    if (a>=b) and (a>=c):
        largest=a
    elif (b>=a) and (b>=c):
        largest=b
    else:
        largest=c
    return largest

a=10
b=20
c=5
print(maximum(a,b,c))

Output:-20


#2. Write a Python function to sum all the numbers in a list

def sum(l):
    result=l[0]+l[1]+l[2]+l[3]
    return result
print(sum([20,30,40,50]))

Output:-140


#3. Write a Python function to multiply all the numbers in a list

def multiply(l):
    result=l[0]*l[1]*l[2]*l[3]*l[4]*l[5]
    return result
print(multiply([2,3,4,5,1,6]))

Output:-720


#4. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters

str=input("Enter string:")
count1=0
count2=0
for i in str:
    if(i.islower()):
        count1+=1
    elif(i.isupper()):
        count2+=1
print("Number of lowercase letters is:",count1)
print("Number of uppercase letters is:",count2)
        
Output:-Enter string:TechnoColabs
        Number of lowercase letters is: 10
        Number of uppercase letters is: 2        



#5. Write a Python program to print the even numbers from a given list

l=[1,2,3,4,5,6]
for i in l:
    if (i%2==0):
        print(i)

Output:-2
        4
        6            