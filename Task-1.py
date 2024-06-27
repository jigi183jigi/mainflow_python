#TASK - 1

# DATATYPES
# CONDITIONAL STATEMENTS
# LOOPS
# ARITHETIC OPERATIONS
# FUNCTIONS
# MANIPULATION OF STRINGS

# Foundational Python Concepts

# Variables -> It is name which can get assigned a value 
# value is assigned using '=' operator

name = 'Nayana'
age = 19
pi = 3.14






# DATA TYPES -> Python has several built in datatypes


# 1) NUMERICAL TYPES -- int, float, Complex

#  Int (inteager) datatype is to get assigned whole numbers
age = 19

#  Float datatype is to get assigned decimal numbers
pi = 3.14

#  Complex datatype is to get assigned imaginary number in the form nj
c = 1j


# 2) TEXT TYPE -- str 

#  String datatype is to get assigned a sequence of characters
name = "jigi"



# 3) SEQUENCE TYPE -- list, Tuple, Range

#  List datatype is to store ordered and mutable collection of items
cities = ["mumbai", "chennai", "delhi"]

#  Tuple datatype is to store ordered and immutable collection of items
direction = ("north", "east", "west", "south")

#  Range datatype 
x = range(5)      # 0, 1, 2, 3, 4
y = range(2,5)    # 2, 3, 4
z = range(1,10,2) # 1, 3, 5, 7, 9


# 4) MAPPING DATATYPE -- dict

#  Dict is used to store un-ordered collection of key-pair values
person = {name : "nayana" , age : 19}


# 5) SET DATATYPE -- set, frozenset

#  Set datatype is used to store mutabled, un-ordered collection of unique items
set1 = {1, 2, 3, 4}
set1.add(5)    # 1, 2, 3, 4, 5
set1.remove(3) # 1, 2, 4, 5

#  Frozenset is immutable version of set.
frozenset1 = frozenset([1, 2, 3, 4])


# 6) BOOLEAN TYPE -- bool

#  Bool datatype is used to store TRUE or FASLE values
t = True
f = False


# 7) NONE TYPE -- none
x = None




# CONDITIONAL DATATYPES -> It allows the execution of different pieces of code based on certain conditions.
  

# 1) if statement : checks whether a condition is true or not
x = 18
if(x > 17): 
    print("you are eligible to vote")

# 2) if else statement : 
if(x > 17):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

# 3) if-else-if statement : more than one consitions
if(age > 32):
    print(" Not eligible to take UPSC")
elif (age < 21):
    print("Not eligible to take UPSC")
else:
    print("Eligible to take UPSC")
    
# 4) Switch Condition : Multiple conditions used as dictionary
switch = { 1: "x is one",
           2: "x is two"
         }
x=1
print(switch.get(x, "x is neither one nor two") )

# 5) Ternary Expression conditional statement : shorthand writing of if-else
eligible_to_vote = True if age>18 else False





# LOOPS -> For, While and Nested Loops

# 1) WHILE loop -- To execute a block of statements repeatedly until a given condition is satisfied.
print("Top 3 rankings")
rank = 1
while(rank <=3 ) :
    print("rank - ",rank)
    rank = rank+1

# 2) FOR Loop --  iterate over a sequence
for i in range(1,4):
    print("rank - ",i)

# 3) NESTED loop -- loop inside another loop 
mat = [ [ 1, 2, 3], 
        [ 1, 2, 3], 
        [ 1, 2, 3], ]
for i in range(3):
    for j in range(3):
        print(mat[i][j],end=" ")
    print("\n")




# ARITHMETIC OPERATIONS -> Addition, Subtraction, 

a = 50
b = 5
c=3

print("Addition a+b=",a+b)
print("Subtraction a-b=",a-b)
print("Multiplication a*b=",a*b)
print("Division a/c=",a/c)
print("floor division a//c=",a//c)
print("Modulus a%b=",a%b)
print("Exponentiation b**c=",b**c)



# FUNCTIONS 

# function with return value
def add(a,b):
    return (a+b)
print(add(5,5))

# function with default parameters
def add(a=5,b=4):
    return(a+b)
print(add())

# function with variable length arguments
def summ(*arr):
    return sum(arr)
print(summ(11,22,33))




# STRING MANIPULATION
#  creating and printing a string
str1 = "Manipulation Of String"

#  accessing a character in a string
print(str1)
print(str1[0])

#  Length of string -- len
print( len(str1) )

#  searching a character in string -- find  , if not found returns -1
print(str1.find("a") )
print(str1.find("S") )
print(str1.find("P") ) #case-sensitive

#  frequency of a character in a string -- count
print(str1.count("i") )
print(str1.count(" ") ) # number of spaces

#  Slicing of string
print( str1[0]) #get one char of the word
print( str1[0:1]) #get one char of the word (same as above)
print( str1[0:3]) #get the first three char
print( str1[:3])#get the first three char
print( str1[-3:]) #get the last three char
print( str1[3:]) #get all but the three first char
print( str1[:-3]) #get all but the three last character

# splitting of string
print(str1.split(' '))

# to uppercase, to lowercase, 
print(str1.upper())
print(str1.lower())

#  reverse a string
print(''.join(reversed(str1)))
print(str1[::-1]) 
