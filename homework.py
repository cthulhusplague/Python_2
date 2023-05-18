Functions, Scoping, Data Collections 1 & List Comprehensions¶
Tasks Today:
Monday Additions (or, and ... if statements)

1) String Manipulation
     a) strip()
     b) title()
2) Working With Lists
     a) min()
     b) max()
     c) sum()
     d) sort()
     e) Copying a List
     f) 'in' keyword
     g) 'not in' keyword
     i) Checking an Empty List
     j) Removing Instances with a Loop
3) List Comprehensions
4) Tuples
     a) sorted()
5) Functions
     a) User-Defined vs. Built-In Functions
     b) Accepting Parameters
     c) Default Parameters
     d) Making an Argument Optional
     e) Keyword Arguments
     f) Returning Values
     g) *args
     h) Docstring
     i) Using a User Function in a Loop
6) Scope

String Manipulation
.lstrip()
# string.lstrip()
name = "      hJohn Smith"
stripped_name = name.lstrip(" " " h")
print(stripped_name)
​
John Smith
.rstrip()
# string.rstrip()
name = "Bill Ross    th"
print(name.rstrip(" " "th"))
​
Bill Ross
.strip()
# string.strip()
name = "  John Smith  "
print(name.strip())
John Smith
.title()
# string.title()
president = "barack obama"
print(president.title())
Barack Obama
String Exercise
Strip all white space and capitalize every name in the list given

names = ['    coNNor', 'max', ' EVan ', 'JORDAN']
# HINT: You will need to use a for loop for iteration
​
for x in names:
    print(x)
stripped_name = names.lstrip('  ',  )
print(stripped_name)
print(names.title)
    coNNor
max
 EVan 
JORDAN
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
/var/folders/6g/hc015g3x1k9dftwggpdsfmgh0000gq/T/ipykernel_2572/291641397.py in <module>
      4 for x in names:
      5     print(x)
----> 6 stripped_name = names.lstrip('  ',  )
      7 print(stripped_name)
      8 print(names.title)

AttributeError: 'list' object has no attribute 'lstrip'

Working With Lists
min()
# min(list)
numbers = [4, 2, 97, 54, 16]
​
print(min(numbers))
2
max()
# max(list)
​
print(max(numbers))
​
97
sum()
# sum(list)
​
print(sum(numbers))
173
sorted()
# sorted(list)
​
print(numbers)
​
sorted_numbers = sorted(numbers)
​
print(sorted_numbers)
[4, 2, 97, 54, 16]
[2, 4, 16, 54, 97]
.sort()
Difference between sort and sorted, is that sorted doesn't change original list it returns a copy, while .sort changes the original list

# list.sort()
print(f'Before Sort: {numbers}')
print(numbers.sort())
print(numbers)
​
# use sorted when you don't want to alter original list, use .sort() when you want to alter original list
Before Sort: [4, 2, 97, 54, 16]
None
[2, 4, 16, 54, 97]
Copying a List
# [:] copies a list, doesn't alter original
list_1 = numbers[:]
print(list_1)
[2, 4, 16, 54, 97]
'in' keyword
l_teachers = ["Joel", "Derek", "Connor", "Brian", "Joe"]
​
# if 'Derek' in l_teachers:
#     print("Coding Temple instructor")
    
# else:
#     print("not an instructor")
    
for name in l_teachers:
    if 'C' in name[0]:
        print('Found')
    else:
        print('Not Found')
Not Found
Not Found
Found
Not Found
Not Found
'not in' keyword
if "Zack" not in l_teachers:
    print('Not a CT instructor')
Not a CT instructor
Checking an Empty List
# if l_1: or if l_1 = []
list_2 = []
​
if list_2 == []:
    print('Wasabi')
​
Wasabi
Removing Instances with a Loop
# while, remove
names = ['Connor', 'Joel', 'Max', 'Evan', 'Rob', 'Evan']
​
while 'Evan' in names:
    names.remove('Evan')
print(names)    
​
# for name in names:
#     if names == 'Evan':
#         names.remove('Evan')
# print(names)    
['Connor', 'Joel', 'Max', 'Rob']
List Exercise
Remove all duplicates
Extra: Create a program that will remove any duplicates from a given list

names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
# Hint 1: You will need an append
# Hint 2: Using an empty list will make life easier
​
list_2 = []
​
names.append('connor')
​
if list_2 == []:
    print(names)
['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin', 'connor']
List Comprehensions
Creating a quickly generated list to work with
*result* = [*transform* *iteration* *filter* ]

In a list comprehension we have a few pieces:
The first is the counter/ variable - IN this the variable is x
then we have a transform for the variable
The finale part of a list comp is called the condition
    [variable, transform, condition]
# number comprehension
​
# With a regular for loop
​
nums = []
​
for i in range(100):
    if i % 2 == 0:
        nums.append(i**2)
print(nums)    
​
# IN a list comprehension we have a few pieces:
# The first is the counter/ variable - IN this the variable is x
# Then we have a transform for the variable 
# The finale part of a list comp is called the condition
#[variable, transform, condition]
​
print('\n')
nums_comp = [i**2 for i in range(100) if i % 2 == 0]
print(nums_comp)
​
​
[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500, 2704, 2916, 3136, 3364, 3600, 3844, 4096, 4356, 4624, 4900, 5184, 5476, 5776, 6084, 6400, 6724, 7056, 7396, 7744, 8100, 8464, 8836, 9216, 9604]


[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500, 2704, 2916, 3136, 3364, 3600, 3844, 4096, 4356, 4624, 4900, 5184, 5476, 5776, 6084, 6400, 6724, 7056, 7396, 7744, 8100, 8464, 8836, 9216, 9604]
There are a few benefits to using List comprehensions. The most obvious would be that we now have shorter code to work with instead of using 3+ lines of code in the for loop variant.

Another is an added benefit to memory usage. Since the list's memory is allocated first before adding elements to it, we don't have to resize the list once we add elements to it.

Lastly, list comprehensions are considered the "pythonic" way to write code by the PEP8 standards (Python Style Guide)

# square number comprehension
​
squares = [x**2 for x in range(10)]
print(squares)
​
print('\n')
​
squares_reg = []
for x in range(10):
    squares_reg.append(x**2)
print(squares_reg)    
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# string comprehension
​
names = ['Connor', 'Max', 'Evan', 'Rob']
​
first_char_comp = [name[0] for name in names]
print(first_char_comp)
​
print('\n')
​
first_char = []
​
for name in names:
    first_char.append(name[0])
print(first_char)
['C', 'M', 'E', 'R']


['C', 'M', 'E', 'R']
c_names = [first_name for first_name in names if first_name[0] == 'C']
print(c_names)
​
c_names_reg = []
​
for first_name in names:
    if first_name[0] == 'C':
        c_names_reg.append(first_name)
print(c_names_reg)        
['Connor']
['Connor']
​
Tuples
Defined as an immutable list


Seperated by commas using parenthesis
tup_1 = 1,2,3 
tup_2 = (1,2,3)
​
# print(type(tup_1))
​
# print(tup_1[0])
​
for number in tup_1:
    print(number)
    
for number in range(len(tup_1)):
    print(tup_1[number])
    
    
1
2
3
1
2
3
sorted()
tup_3 = (20, 5, 1, 3, 9, 45)
​
sorted_tup = sorted(tup_3)
print(sorted_tup)
​
# Sorted WILL return list
​
random_list = [3, 4, 66, 7, 33]
combine_list = sorted_tup + random_list
​
new_tup = tuple(combine_list)
​
print(new_tup)
[1, 3, 5, 9, 20, 45]
(1, 3, 5, 9, 20, 45, 3, 4, 66, 7, 33)
Adding values to a Tuple
print(tup_1)
​
tup_1 = tup_1 + (5,)
print(tup_1)
(1, 2, 3, 5)
(1, 2, 3, 5, 5)
Functions
User-Defined vs. Built-In Functions
# User defined!
​
def sayHello():
    return 'Hello World'
​
sayHello()
​
​
Hello World
Accepting Parameters
# ARGUMENTS or PARAMETERS
# Order Matters
# a variable can be any type of object
​
def printFullName(first_name, last_name):
    return f'Hello, {first_name} {last_name}'
​
a_name = input('What is your first name? ')
​
printFullName('Joel', 'Carter')
​
printFullName(a_name, 'Hammond')
What is your first name? Logan
'Hello, Logan Hammond'
Default Parameters
# Default parameters need to be declared AFTER non-default parameters
​
def printAgentName(first_name, last_name = 'Bond'):
    return f'The name is {last_name}...{first_name} {last_name}!'
​
print(printAgentName('Logan'))
​
# DON'T DO THIS
def printAgentAgain(last_name = 'ever', first_name):
    return f'Last name {last_name}, first name {first_name}!'
​
print(printAgentAgain(first_name = "Greatest"))
  File "/var/folders/6g/hc015g3x1k9dftwggpdsfmgh0000gq/T/ipykernel_1697/1291139366.py", line 9
    def printAgentAgain(last_name = 'ever', first_name):
                                                      ^
SyntaxError: non-default argument follows default argument


Making an Argument Optional
def printHorseName(first, middle ='', last = 'Ed'):
    return f'Hello {first} {middle} {last}'
​
printHorseName('Mr')
'Hello Mr  Ed'
Keyword Arguments
def printSuperHero(name, power = 'flying'):
    return f"The hero's name is {name} and superpower is {power}"
​
printSuperHero('Superman')
"The hero's name is Superman and superpower is flying"
Creating a start, stop, step function
def my_range(stop, start=0, step=1):
    for i in range(start,stop,step):
        print(i)
        
my_range(20)        
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
Returning Values
def addNums(num1, num2):
    return num1 + num2
​
addNums(5,2)
7
*args
# args stands for arguments and takes ANY number of arguments as parameters
# must be last if multiple parameters are present
def printArgs(num1, *args, **kwargs):
    print(num1)
    print(args)
    print(kwargs)
    
    for arg in args:
        print(arg)
        
        for kwarg in kwargs:
            print(kwarg)
    
printArgs(36, 'DragonZord', 'Vanilla', 2, 3, testing="joel")    
36
('DragonZord', 'Vanilla', 2, 3)
{'testing': 'joel'}
DragonZord
testing
Vanilla
testing
2
testing
3
testing
Docstring
def printNames(list_1):
    '''
        printNames(list_1)
        Function requires a list to be passed as a parameter
        and will print the contents of a list. Expecting a list of 
        names(strings) to be passed.
    '''
    for name in list_1:
        print(name)
        
printNames(['George', 'Ramon', 'Peter'])
help(printNames)
George
Ramon
Peter
Help on function printNames in module __main__:

printNames(list_1)
    printNames(list_1)
    Function requires a list to be passed as a parameter
    and will print the contents of a list. Expecting a list of 
    names(strings) to be passed.

Using a User Function in a Loop
def printInput(answer):
    print(answer)
    
response = input('Are you ready to quit? ')
​
while True:
    ask = input('What do you want to do? ')
    printInput(ask)
    
    response = input('Ready Yet? ')
    if response.lower() == 'quit':
        break
Are you ready to quit? No
What do you want to do? I don't know
I don't know
Ready Yet? quit
Function Exercise
Write a function that loops through a list of first_names and a list of last_names, combines the two and return a list of full_names

first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']
​
# Output: ['John Smith', 'Evan Smith', 'Jordan Williams', 'Max Bell']
​
def printFullName(first_name, last_name):
    return ['John Smith', 'Evan Smith', 'Jordan Williams', 'Max Bell']
​
printFullName('John', 'Smith')
['John Smith', 'Evan Smith', 'Jordan Williams', 'Max Bell']
Scope
Scope refers to the ability to access variables, different types of scope include:
a) Global
b) Function (local)
c) Class (local)

 number = 3 
#     Global Variable; accessiable ANYWHERE in my code
​
def myFunc():
    number = 6
    number += 4
#     ^ Local function variable
    return number
​
print(number + 4)
print(myFunc())
7
10
Exercises
Exercise 1
Given a list as a parameter,write a function that returns a list of numbers that are less than ten


For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

# Use the following list - [1,11,14,5,8,9]
​
l_1 = [1,11,14,5,8,9]
​
def my_range(stop, start=0, step=1):
    for i in range(start, stop, step):
        print(i)
my_range(10)
0
1
2
3
4
5
6
7
8
9
Exercise 2
Write a function that takes in two lists and returns the two lists merged together and sorted
Hint: You can use the .sort() method

a, list_b
1
l_1 = [1,2,3,4,5,6]
2
l_2 = [3,4,5,6,7,8,10]
3
​
4
​
5
list_a = [1,2,3,4,5,6]
6
list_b =[3,4,5,6,7,8,10]
7
​
8
​
9
def myList(list_a, list_b):
10
    merged = list_a + list_b
11
    merged.sorted()
12
    return merged
13
​
14
printmyList(list_a, list_b)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
/var/folders/6g/hc015g3x1k9dftwggpdsfmgh0000gq/T/ipykernel_1758/2768738896.py in <module>
     12     return merged
     13 
---> 14 printmyList()

NameError: name 'printmyList' is not defined