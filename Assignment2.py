#Qu.1 Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

for i in range(2000,3201):
    if i%7==0 and i%5!=0:
            print(i, end=",")
       
Output: 2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199,     


#Qu.2 Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

n = int(input("Enter a number for factorial:"))
fact = 1
for i in range(1,n+1):
    fact=fact*i
print(fact)    

output: Enter a number for factorial:6 
        720


#Qu.3 With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}   

n=int(input("Enter a number:"))
ans={i:i*i for i in range(1,n+1)}
print(ans)

output: Enter a number:7
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

#Qu.4 Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

st=input("Enter the numbers:").split(",")
tpl=tuple(lst)
print(lst)
print(tpl)

Output: Enter the numbers:45,36,98,34,12,19,20,68
['45', '36', '98', '34', '12', '19', '20', '68']
('45', '36', '98', '34', '12', '19', '20', '68')


#Qu.5 Define a class which has at least two methods:
# a) getString: to get a string from console input
# b) printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class IOstring():
    def ___init__(self):
        pass
    def getString(self):
        self.s=input("Enter a string:")
    def printString(self):
        print(self.s.upper()) 

i=IOstring()
i.getString()
i.printString()           

Output: Enter a string:assignment
        ASSIGNMENT


#Qu.6 Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:
#100,150,180
#The output of the program should be:
#18,22,24   
 
from math import*
C = 50
H = 30
def calculate(D):
    return sqrt((2*C*D)/H)

D=input("Enter the numbers:").split(",")
D=[int(i) for i in D]
D=[calculate(i) for i in D]
D=[round(i) for i in D]
D=[str(i) for i in D]

print(",".join(D))

Output: Enter the numbers:100,125,256
         18,20,29


#Qu.7 Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i * j.
#Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
         
x,y = map(int,input("Enter two numbers:").split(","))
lst = []
for i in range(x):
    tmp=[]
    for j in range(y):
        tmp.append(i*j)
    lst.append(tmp)

print(lst)        

Output: Enter two numbers:2,4
        [[0, 0, 0, 0], [0, 1, 2, 3]]


#Qu.8 Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world

lst = input("Enter few words separated by commas:").split(",")
lst.sort()
print(",".join(lst))

Output: Enter few words separated by commas:hello,apple,world,computer
        apple,computer,hello,world


#Qu.9 Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect
#Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT

lst=[]
while True:
    x = input()
    if len(x)==0:
        break;
    lst.append(x.upper())
for line in lst:
    print(line)     

Output: hello world
        i am mansi

        HELLO WORLD
        I AM MANSI    


#Qu.10 Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
#Suppose the following input is supplied to the program:
#hello world and practice makes perfect and hello world again
#Then, the output should be:
#again and hello makes perfect practice world  

word = input("Enter few words separated by whitespaces:").split()
for i in word:
    if word.count(i)>1:
       word.remove(i)
word.sort()
print(" ".join(word))   

Output: Enter few words separated by whitespaces: hello world and practice makes perfect and hello world again
        again and hello makes perfect practice world


#Qu.11 Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#Example:0100,0011,1010,1001
#Then the output should be:1010

def check(x):
    return int(x,2)%5==0
data = input("Enter 4 digit binary numbers separated by commas:").split(",")
data = list(filter(check,data))     
print(",".join(data))   

Output: Enter 4 digit binary numbers separated by commas:1010,1100,1011,0011,1110
        1010


#Qu.12 Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

def check(element):
    return all(ord(i)%2==0 for i in element)
lst = [str(i) for i in range(1000,3001)]
lst = list(filter(check,lst))
print(",".join(lst))    

Output: 2000,2002,2004,2006,2008,2020,2022,2024,2026,2028,2040,2042,2044,2046,2048,2060,2062,2064,2066,2068,2080,2082,2084,2086,2088,2200,2202,2204,2206,2208,2220,2222,2224,2226,2228,2240,2242,2244,2246,2248,2260,2262,2264,2266,2268,2280,2282,2284,2286,2288,2400,2402,2404,2406,2408,2420,2422,2424,2426,2428,2440,2442,2444,2446,2448,2460,2462,2464,2466,2468,2480,2482,2484,2486,2488,2600,2602,2604,2606,2608,2620,2622,2624,2626,2628,2640,2642,2644,2646,2648,2660,2662,2664,2666,2668,2680,2682,2684,2686,2688,2800,2802,2804,2806,2808,2820,2822,2824,2826,2828,2840,2842,2844,2846,2848,2860,2862,2864,2866,2868,2880,2882,2884,2886,2888


#Qu.13 Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
# Then, the output should be:
#LETTERS 10
#DIGITS 3

word = input("Enter some data:")
letter,digit = 0,0
for i in word:
    letter+=i.isalpha()
    digit+=i.isnumeric()
print("LETTERS {0}\nDIGITS {1}".format(letter,digit))    

Output: Enter some data:hello world 12345
        LETTERS 10
        DIGITS 5


#Qu.14 Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#Suppose the following input is supplied to the program:
#Hello world!
#Then, the output should be:
#UPPER CASE 1
#LOWER CASE 9

string = input("Enter a sentence:")
upper,lower = 0,0
for i in string:
    if i.isupper()==True:
        upper+=1
    if i.islower()==True:
        lower+=1
print("UPPER CASE: ",upper)
print("LOWER CASE: ",lower)            

Output: Enter a sentence:HELLO everyone
        UPPER CASE:  5
        LOWER CASE:  8
        

#Qu.15 Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#Suppose the following input is supplied to the program:
#9
#Then, the output should be:
#11106 

a = input("Enter a number:")
total = int(a)+int(2*a)+int(3*a)+int(4*a)
print(total)

Output: Enter a number:2
        2468


#Qu.16 Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. Suppose the following input is supplied to the program:
#1,2,3,4,5,6,7,8,9
#Then, the output should be:
#1,9,25,49,81      

lst = [str(int(i)**2) for i in input("Enter few numbers separated by commas:").split(",") if int(i)%2!=0]
print(",".join(lst))

Output: Enter few numbers separated by commas:1,2,3,4,5,6,7,8,9
        1,9,25,49,81


#Qu.17   Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
#D 100
#W 200
#D means deposit while W means withdrawal.
#Suppose the following input is supplied to the program:
#D 300
#D 300
#W 200
#D 100
#Then, the output should be:
#500      

account = 0
while True:
    action = input("Deposit/Withdrawal/Balance/Quit?D/W/B/Q? ").lower()
    if action == "d":
        deposit = input("How much do you want to deposit: ")
        account = account+int(deposit)
    elif action == "w":
        withdraw = input("How much do you want to withdraw: ")
        account = account-int(withdraw)
    elif action == "b":
        print(account)
    else:
        quit()                

Output: Deposit/Withdrawal/Balance/Quit?D/W/B/Q? d
        How much do you want to deposit: 500
        Deposit/Withdrawal/Balance/Quit?D/W/B/Q? w
        How much do you want to withdraw: 200
        Deposit/Withdrawal/Balance/Quit?D/W/B/Q? b
        300
        Deposit/Withdrawal/Balance/Quit?D/W/B/Q?


#Qu.18 A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
#Following are the criteria for checking the password:
#At least 1 letter between [a-z]
#At least 1 number between [0-9]
#At least 1 letter between [A-Z]
#At least 1 character from [$#@]
#Minimum length of transaction password: 6
#Maximum length of transaction password: 12
#Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
#Example
#If the following passwords are given as input to the program:
#ABd1234@1,a F1#,2w3E*,2We3345
#Then, the output of the program should be:
#ABd1234@1            

def is_low(x):
    for i in x:
        if "a"<=i and i<="z":
            return True
    return False 
def is_up(x):
    for i in x:
        if "A"<=i and i<="Z":
            return True
    return False
def is_num(x):
    for i in x:
        if "0"<=i and i<="9":
            return True
    return False
def is_other(x):
    for i in x:
        if i=="$" or i=="#" or i=="@":
            return True
    return False
s = input("Enter passwords:").split(",")
lst = []
for i in s:
    length = len(i)
    if (6<=length and length<=12 and is_low(i) and is_up(i) and is_num(i) and is_other(i)):
        lst.append(i)
print(",".join(lst))                             

Output: Enter passwords:Mansi@1999,Anjana@123,mansi,1234,@#$
        Mansi@1999,Anjana@123


#Qu.19 You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:
#1: Sort based on name
#2: Then sort based on age
#3: Then sort by score
#The priority is that name > age > score.
#If the following tuples are given as input to the program:
#Tom,19,80
#John,20,90
#Jony,17,91
#Jony,17,93
#Json,21,85
#Then, the output of the program should be:
#[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

lst = []
while True:
    s = input("Enter name,age,score: ").split(",")
    if not s[0]:
        break
    lst.append(tuple(s))
lst.sort(key = lambda x:(x[0],x[1],x[2]))    
print(lst)

Output: Enter name,age,score: Tom,19,90
Enter name,age,score: John,20,80
Enter name,age,score: Jony,17,91
Enter name,age,score: Jony,17,93
Enter name,age,score: Json,21,85
Enter name,age,score: 
[('John', '20', '80'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '90')]


#Qu.20 Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

class Divisible:
    def by_seven(self,n):
        for number in range(n+1):
            if number%7==0:
                yield number

divisible=Divisible()
generator=divisible.by_seven(int(input("Enter a number: ")))  
for number in generator:
    print(number)              

Output: Enter a number: 50
        0
        7
        14
        21
        28
        35
        42
        49


#Qu.21  A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#Then, the output of the program should be:
#2              

import math
x,y=0,0
while True:
    s=input().split()
    if not s:
        break
    if s[0] == "UP": #s[0] indicates command
        x-=int(s[1])  #s[1] indicates unit of move
    if s[0] == "DOWN":
        x+=int(s[1])
    if s[0] == "LEFT":
        y-=int(s[1])
    if s[0] == "RIGHT":
        y+=int(s[1])

dist=round(math.sqrt(x**2+y**2)) #euclidian distance = square root of (x^2+y^2) and rounding it to nearest integer
print(dist)                 

Output: UP 5
        DOWN 3
        LEFT 3
        RIGHT 2

        2


#Qu.22 Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
#Suppose the following input is supplied to the program:
#New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
#Then, the output should be:
#2:2
#3.:1
#3?:1
#New:1
#Python:5
#Read:1
#and:1
#between:1
#choosing:1
#or:2
#to:1        

ss = input().split()
word=sorted(set(ss))
for i in word:
    print("{0}:{1}".format(i,ss.count(i)))

Output: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
        2:2
        3.:1
        3?:1
        New:1
        Python:5
        Read:1
        and:1
        between:1
        choosing:1
        or:2
        to:1    


#Qu.23 Write a method which can calculate square value of number

n = int(input("Enter a number: "))
print(n**2)

Output: Enter a number: 6
        36


#Qu.25 Define a class, which have a class parameter and have a same instance parameter.

class Car:
    name="Car"

    def __init__(self,name = None):
        self.name = name

honda = Car("Honda")
print("%s name is %s"%(Car.name,honda.name))

toyota = Car()
toyota.name="Toyota"
print("%s name is %s"%(Car.name,toyota.name))

Output: Car name is Honda
Car name is Toyota


#Qu.26 Define a function which can compute the sum of two numbers.

sum = lambda x,y:x+y
print(sum(1,2))

Output: 3


#Qu.27 Define a function that can convert a integer into a string and print it in console.

def convert(n):
    return str(n)
x=convert(10)
print(x) 
print(type(x))   

Output: 10
        <class 'str'>


#Qu.28   Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.
      
def sum(a,b):
    return int(a)+int(b)

print(sum("10","20"))    

Output: 30


#Qu.29 Define a function that can accept two strings as input and concatenate them and then print it in console.

def concatenate(s1,s2):
    return s1+s2

print(concatenate("10","45"))    

Output: 1045


#Qu.30 Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

def maxLength(a,b):
    l1 = len(a)
    l2 = len(b)
    if l1>l2:
        print(a)
    elif l1<l2:
        print(b)
    else:
        print(a)
        print(b)

a,b = input("Enter two strings separated by comma: ").split(",")
maxLength(a,b)               

Output: Enter two strings separated by comma: Technocolabs,Python
        Technocolabs


#Qu.31 Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

def printDict():
    dict = {i:i**2 for i in range(1,21)}
    print(dict)

printDict()    

Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400}


#Qu.32 Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

def printDict():
    dict = {i:i**2 for i in range(1,21)}
    print(dict.keys())

printDict()    

Output: dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


#Qu.33 Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

def printList():
    lst = [i**2 for i in range(1,21)]
    print(lst)

printList()    

Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]


#Qu.34 Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

def printList():
    lst = [i**2 for i in range(1,21)]
    for i in range(5):
        print(lst[i])
printList()        

Output: 1
        4
        9
        16
        25


#Qu.35 Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

ef printList():
    lst = [i**2 for i in range(1,21)]
    for i in range(19,14,-1):
        print(lst[i])

printList()        

Output: 400
        361
        324
        289
        256


#Qu.36 Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

def printList():
    lst = [i**2 for i in range(1,21)]
    for i in range(5,20):
        print(lst[i])

printList()        

Output: 36
        49 
        64
        81
        100
        121
        144
        169
        196
        225
        256
        289
        324
        361
        400


#Qu.37 Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

def printTuple():
    t = [i**2 for i in range(1,21)]
    print(tuple(t))

printTuple()    

Output: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400)


#Qu.38 With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

tpl = (1,2,3,4,5,6,7,8,9,10)
print(tpl[:5])
print(tpl[5:])

Output: (1, 2, 3, 4, 5)
        (6, 7, 8, 9, 10)


#Qu.39 Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

t1 = (1,2,3,4,5,6,7,8,9,10)
t2 = tuple(i for i in t1 if i%2==0)
print(t2)

Output: (2, 4, 6, 8, 10)


#Qu.40 Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

text = input("Please enter something: ")
if text == "yes" or text == "YES" or text == "Yes":
    print("Yes")
else:
    print("No")    

Output: Please enter something: yes
        Yes 
        Please enter something: python
        No


#Qu.41  Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

l = [1,2,3,4,5,6,7,8,9,10]
sqrNum = map(lambda x:x**2,l)
print(list(sqrNum))

Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#Qu.42 Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

def even(x):
    return x%2==0
def sqr(x):
    return x*x
l = [1,2,3,4,5,6,7,8,9,10]
evenNum = map(sqr,filter(even,l))
print(list(evenNum))

Output: [4, 16, 36, 64, 100]


#Qu.43 Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

def even(x):
    return x%2==0
evenNum = filter(even,range(1,21)) 
print(list(evenNum))   

Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


#Qu.44 Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

sqrNum = map(lambda x:x**2,range(1,21))
print(list(sqrNum))

Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]


#Qu.45 Define a class named American which has a static method called printNationality.

class American:
    @staticmethod
    def printNationality():
        print("I am American")

American.printNationality()        

Output: I am American


#Qu.46 Define a class named American and its subclass NewYorker.

class American():
    print("I am american")

class NewYorker(American):
    print("I am newyorker")

american=American()
newyorker=NewYorker()

print(american)
print(newyorker)

Output: I am american
        I am newyorker
        <__main__.American object at 0x000002562CB07088>
        <__main__.NewYorker object at 0x000002562CB07108>


#Qu.47 Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.14*(self.radius**2) 

circle = Circle(5)
print(circle.area())           

Output: 78.5


#Qu.48 Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

class Rectangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w
    def area(self):
        return self.length*self.width 

rectangle = Rectangle(2,4)
print(rectangle.area())

Output: 8


#Qu.49 Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length=0):
        Shape.__init__(self)
        self.length=length
    def area(self):
        return self.length*self.length

sqr = Square(5)        
print(sqr.area())
print(Square().area())

Output: 25
        0


#Qu.50 Please raise a RuntimeError exception.

raise RuntimeError("something wrong")

Output: Traceback (most recent call last):
          File "f:/Python/Practice.py", line 1, in <module>
            raise RuntimeError("something wrong")
        RuntimeError: something wrong


#Qu.51 Write a function to compute 5/0 and use try/except to catch the exceptions.

def division():
    return 5/0

try:
    division() 
except ZeroDivisionError as ze:
    print("Why on earth you are dividing by ZERO!!!!!!")
except:
    print("Any other exception")           

Output: Why on earth you are dividing by ZERO!!!!!!


#Qu.52 Define a custom exception class which takes a string message as attribute.

class CustomException(Exception):
    def __init__(self,message):
        self.message = message
num = int(input("Enter a number: ")) 
try:
    if num<10:
        raise CustomException("Input is less than 10")
    elif num>10:
        raise CustomException("Input is greater than 10")
except CustomException as ce:
    print("The error raised: "+ce.message)           

Output: Enter a number: 25
        The error raised: Input is greater than 10 
        Enter a number: 5
        The error raised: Input is less than 10  


#Qu.53 Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
#Example: If the following email address is given as input to the program:
#john@google.com
#Then, the output of the program should be:
#john
#In case of input data being supplied to the question, it should be assumed to be a console input.       

email = "john@google.com"
email = email.split("@")
print(email[0])

Output: john


#Qu.55 Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
#Example: If the following words is given as input to the program:
#2 cats and 3 dogs.
#Then, the output of the program should be:
#['2', '3']
#In case of input data being supplied to the question, it should be assumed to be a console input.

import re

email = input("Enter some data: ")
pattern = "\d+"
ans = re.findall(pattern,email)
print(ans)

Output: Enter some data: 2 cats and 3 dogs
['2', '3']


#Qu.56 Print a unicode string "hello world".

unicodeString = u"hello world!"
print(unicodeString)

Output: hello world!


#Qu.59 Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
#Example: If the following n is given as input to the program:
#5
#Then, the output of the program should be:
#3.55
#In case of input data being supplied to the question, it should be assumed to be a console input.

n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    sum+=i/(i+1)
print(round(sum,2))    

Output: Enter a number: 5
        3.55


#Qu.60 Write a program to compute:
#f(n)=f(n-1)+100 when n>0
#and f(0)=0
#with a given n input by console (n>0).
#Example: If the following n is given as input to the program:
#5
#Then, the output of the program should be:
#500
#In case of input data being supplied to the question, it should be assumed to be a console input.

def f(n):
    if n==0:
        return 0
    return f(n-1)+100 

n = int(input("Enter a number: "))
print(f(n))       

Output: Enter a number: 7
        700


#Qu.61 The Fibonacci Sequence is computed based on the following formula:
#f(n)=0 if n=0
#f(n)=1 if n=1
#f(n)=f(n-1)+f(n-2) if n>1
#Please write a program to compute the value of f(n) with a given n input by console.
# Example: If the following n is given as input to the program:
#7
#Then, the output of the program should be:
#13
#In case of input data being supplied to the question, it should be assumed to be a console input.

def f(n):
    if n<2:
        return n
    return f(n-1)+f(n-2)

n = int(input("Enter a number: "))
print(f(n))        

Output: Enter a number: 10 
        55 


#Qu.62 The Fibonacci Sequence is computed based on the following formula:
#f(n)=0 if n=0
#f(n)=1 if n=1
#f(n)=f(n-1)+f(n-2) if n>1
#Please write a program to compute the value of f(n) with a given n input by console.
#Example: If the following n is given as input to the program:
#7
#Then, the output of the program should be:
#0,1,1,2,3,5,8,13
#In case of input data being supplied to the question, it should be assumed to be a console input.   

def f(n):
    if n<2:
        fibo[n] = n
        return fibo[n]
    fibo[n] = f(n-1)+f(n-2) 
    return fibo[n] 
n = int(input("Enter a number: ")) 
fibo = [0]*(n+1) 
f(n) 
fibo = [str(i) for i in fibo] 
ans = ",".join(fibo) 
print(ans)

Output: Enter a number: 9
        0,1,1,2,3,5,8,13,21,34


#Qu.63 Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
#Example: If the following n is given as input to the program:
#10
#Then, the output of the program should be:
#0,2,4,6,8,10
#In case of input data being supplied to the question, it should be assumed to be a console input.   
     
def evenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1

n=int(input("Enter a number: "))
values = []
for i in evenGenerator(n):
    values.append(str(i)) 
print(",".join(values))            

Output: Enter a number: 15
        0,2,4,6,8,10,12,14


#Qu.64 Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
#Example: If the following n is given as input to the program:
#100
#Then, the output of the program should be:
#0,35,70
#In case of input data being supplied to the question, it should be assumed to be a console input.        

def generate(n):
    for i in range(n+1):
        if i%35==0:
            yield i
n = int(input("Enter a number: "))
res = [str(i) for i in generate(n)] 
print(",".join(res))             

Output: Enter a number: 150
        0,35,70,105,140


#Qu.66 Please write a program which accepts basic mathematic expression from console and print the evaluation result.
#Example: If the following n is given as input to the program:
#35 + 3
#Then, the output of the program should be:
#38

exp = input("Enter a mathematical expression: ")
ans = eval(exp)
print(ans)

Output: Enter a mathematical expression: 25*4
        100


#Qu.68 Please generate a random float where the value is between 10 and 100 using Python module.

import random as r
num = r.uniform(10,100)
print(num)

Output: 10.847159529689552


#Qu.69 Please generate a random float where the value is between 5 and 95 using Python module.

import random 
num = random.uniform(5,95)
print(num)

Output: 51.30097865787027


#Qu.70 Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

import random 
res = [i for i in range(0,11,2)]
print(random.choice(res))

Output: 10


#Qu.71 Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.

import random 
res = [i for i in range(10,151) if i%35==0]
print(random.choice(res))

Output: 35


#Qu.72 Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

import random 
res = random.sample(range(100,201),5)
print(res)

Output: [147, 130, 104, 116, 118]


#Qu.73 Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

import random 
res = random.sample(range(100,201,2),5)
print(res)

Output: [186, 162, 194, 200, 144]


#Qu.74 Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

import random 
lst = [i for i in range(1,1001) if i%35==0]
res = random.sample(lst,5)
print(res)

Output: [910, 770, 175, 490, 420]


#Qu.75 Please write a program to randomly print a integer number between 7 and 15 inclusive.

import random 
print(random.randrange(7,15))

Output: 7


#Qu.77 Please write a program to print the running time of execution of "1+1" for 100 times.

import time
before  = time.time()
for i in range(100):
    x = 1+1
after = time.time()
execution_time = after-before
print(execution_time)

Output: 0.0


#Qu.78 Please write a program to shuffle and print the list [3,6,7,8].

import random
lst = [3,6,7,8]
random.shuffle(lst)
print(lst)

Output: [6, 7, 8, 3]


#Qu.79 Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

subjects=["I","You"]
verbs=["Play","Love"]
objects=["Hockey","Football"]
for sub in subjects:
    for verb in verbs:
        for obj in objects:
            print("{} {} {}".format(sub,verb,obj))

Output: I Play Hockey
        I Play Football
        I Love Hockey
        I Love Football
        You Play Hockey
        You Play Football
        You Love Hockey
        You Love Football


#Qu.80 Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

l = [5,6,77,45,22,12,24]
lst = list(filter(lambda n:n%2!=0,l))
print(lst)

Output: [5, 77, 45]


#Qu.81 By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

l = [12,24,35,70,88,120,155]
l = [x for x in l if x%35!=0]
print(l)

Output: [12, 24, 88, 120, 155]


#Qu.82 By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

l = [12,24,35,70,88,120,155]
l1 = []
for i in range(len(l)):
    if i%2!=0:
        l1.append(l[i])
print(l1)        

Output: [24, 70, 120]


#Qu.83 By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

l = [12,24,35,70,88,120,155]
l = [l[i] for i in range(len(l)) if i!=2 and i!=4]
print(l)

Output: [12, 24, 70, 120, 155]


#Qu.84 By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

array = [[[0 for col in range(8)] for col in range(5)] for row in range (3)]
print(array)

Output: [[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 
0, 0], [0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]]


#Qu.85 By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

l = [12,24,35,70,88,120,155]
l = [l[i] for i in range(len(l)) if i!=0 and i!=4 and i!=5]
print(l)

Output: [24, 35, 70, 155]


#Qu.86 By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

l = [12,24,35,70,88,120,155]
l.remove(24)
print(l)

Output: [12, 35, 70, 88, 120, 155]


#Qu.87 With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

l1 = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]
s1 = set(l1)
s2 = set(l2)
intersection = s1 & s2
print(list(intersection))

Output: [35]


#Qu.88 With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

l = [12,24,35,24,88,120,155,88,120,155]
for i in l:
    if l.count(i)>1:
        l.remove(i)
print(l)        

Output: [12, 35, 24, 88, 120, 155]


#Qu.89 Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

class Person(object):
    def getGender(self):
        return "Unknown"

class Male(Person):
    def getGender(self):
        return "Male" 

class Female(Person):
    def getGender(self):
        return "Female"

male = Male()
female = Female()
male.getGender()
female.getGender()  

Output: Male
        Female


#Qu.90 Please write a program which count and print the numbers of each character in a string input by console.
#Example: If the following string is given as input to the program:
#abcdefgabc
#Then, the output of the program should be:
#a,2
#c,2
#b,2
#e,1
#d,1
#g,1
#f,1

s = input("Enter few words: ")
for letter in range(ord('a'),ord('z')+1):
    letter = chr(letter)
    cnt = s.count(letter)
    if cnt>0:
        print("{}:{}".format(letter,cnt))                    

Output: Enter few words: helloeveryone 
        e:4
        h:1
        l:2
        n:1
        o:2
        r:1
        v:1
        y:1 


#Qu.91 Please write a program which accepts a string from console and print it in reverse order.
#Example: If the following string is given as input to the program:*
#rise to vote sir
#Then, the output of the program should be:
#ris etov ot esir

s = input("Enter something: ")
s = "".join(reversed(s))
print(s)

Output: Enter something: rise to vote sir
        ris etov ot esir


#Qu.92 Please write a program which accepts a string from console and print the characters that have even indexes.
#Example: If the following string is given as input to the program:
#H1e2l3l4o5w6o7r8l9d
#Then, the output of the program should be:
#Helloworld

s = "H1e2l3l4o5w6o7r8l9d"
s = [s[i] for i in range(len(s)) if i%2==0]
print("".join(s))

Output: Helloworld


#Qu.93 Please write a program which prints all permutations of [1,2,3]

import itertools
print(list(itertools.permutations([1,2,3])))

Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1


#Qu.98 You are given a date. Your task is to find what the day is on that date.
#Input
#A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.
#08 05 2015
#Output
#Output the correct day in capital letters.
#WEDNESDAY

import calendar
month,day,year = map(int,input("Enter date in mm dd yyyy format: ").split())
dayId = calendar.weekday(year,month,day)
print(calendar.day_name[dayId].upper())

Output: Enter date in mm dd yyyy format: 08 05 2015
        WEDNESDAY


#Qu.101 You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.
#If the following string is given as input to the program:
#aabbbccde
#Then, the output of the program should be:
#b 3
#a 2
#c 2
#d 1
#e 1 

word = input("Enter something: ")
dct = {}
for i in word:
    dct[i] = dct.get(i,0)+1

dct = sorted(dct.items(),key = lambda x:(-x[1],x[0]))
for i in dct:
    print(i[0]+''+str(i[1]))    

Output: Enter something: hello everyone
        e4
        l2
        o2
         1 
        h1
        n1
        r1
        v1
        y1  


#Qu.103 Given a number N.Find Sum of 1 to N Using Recursion
#Input
#5
#Output
#15 

def rec(n):
    if n==0:
        return n
    return rec(n-1)+n

n = int(input("Enter a number: "))
sum = rec(n)
print(sum)

Output: Enter a number: 5 
        15