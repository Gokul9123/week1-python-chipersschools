########################Printing Hello World###############################
print("Hello")
print("Hello World")

################################Comments####################################
#This is a comment

'''
Every line executed in python is either
 1)Statement
 2)Expression
'''

"""
My Name Is Shashank
"""

############################Data Types#######################################
print(isinstance("a",str))
print(isinstance("a",int))
print(isinstance(2,str))
print(isinstance("a",object))
print(isinstance(2,object))
print(isinstance(print,object))

a=255
print(a)
a="a"
print(a)
type(a)
print(id(a))
b=200
print(id(b))
c=278
print(id(c))

a="aaaaa"
print(id(a))
b="aaaaa"
print(id(b))

a=5677453456754535246681255632435678456789765463
print(a+1) 
#class3-from chippers schools

print("GOKUL")
print(1)

#Print can exhibit any number of argument
print(1,2,3,4,5,6)
print(1,2,3,"gokul",3.4,1+5j)
print(1,2,3,"gokul",3.4,1+5j,sep=",")

print("Hello")
print("World!")

print("a")
print("b")
print("c")

print("a",end=")")
print("b")
print("c")

print("Hello",end=";")
print("World!")

  
#class4--from chipper schols

###########################Taking User Input################################
#Delimiter is \n character
a=input()
print(a)
print(type(a))
#Sample python code
a=input()
b=input()
print(a)
print(b)
#Input in python is delimited using \n by default

###########################Type Casting#####################################
a=65
bin(65)


###########################Typecoercion#####################################
#To do type concersion we use coersioning
a=15
print(str(a))
print(int('12345'))
print(float('1.5'))


#Python doesn't have type casting
a=65
isinstance(a,object)
a='A'
isinstance(a,object)
#In python the above is different


#class5-Operators and Expressions-CipherSchools.py
#Arithmetic Operators
print(5+5)
print(10-5)
print(10/3) #Dividing int by int gives int in python2, but not in python 3
print(isinstance(10.0,int))
print(10//3) #Floor Division
print(10%3)
print(2*3)
print(2**3) #Exponentiation
print("gokul"+"bodangi")
print("abc"*6)
print("gokul" + "bodangi") #String Concatenation

#Comparision Operators
print(1==2)
print(1!=2)
print(1<2)
print(2>3)
print("ab"<"z") #Lexicographical comparison---> Follows dictionary order
print("a"<"A") #Dunders

#Logical Operators
print(True and False)
print(True or False)
print(True and 1)
print(1 and 0)
print(1 and 5)
print(isinstance(True,int)) #Returns True--->True is integer
print(type(True))
print(bool(1))
#Short Curcuiting
'''
a or b=a(if a is truthy)
a or b=b(if a is falsy)
a and b=b(if a is truthy)
a and b=a(if a is falsy)
'''
'''
True or b=True
False or b=b
True or b=b
False or b=False
'''
#Without knowing b we get the result
#Mathematical Beauty!
print("gokul" and 6)
print("" and 6)
print(1.6 or "")
print("" or 2.5)
print(bool(""))
print(bool([]))
print(bool([1,2,3]))
print("" and 0)
print(112 and 0)
print(112 and "")


  
#class6-Conditional Statements(if-elif-else)-CipherSchools.py
############################Control Flow Statements#############################
#Conditional Statements

a=True
if True:                         #Colon in python represents starting of a block
    print("the value is true")   #1 indent= 2 spaces, 4 spaces, 8 spaces
print("end")


a=False
if a:
    print("this value is true")
else:
    print("this value is false")

a=5
if a==3:
    print("this value is 3")
elif a==5:
    print("this value is 5")
else:
    print("this value is not 3 or 5")


#What's not cool with this approach???

if x<0:
    sign=-1
if x==0:
    sign=0
if x>0:
    sign=1

#It will check every if conditions
#q = Can A access profile B
a= isFriend
b= isBlocked
c= isAdmin
d= isMarkZuckerburg
if (condition):
    print("has access")
else:
    print("access denied")

111  
#class7-Looping Statements(while, for)-CipherSchools.py
#while Loop

a=1
while a<10:
    print(a)
    a+=1
#When do we use while and for?

#If we don,t know how many iteration will it take to end this loop
#then we use while loop
#E.g: Temple Run


#for Loop
#Python for loop works on the concept of sequences
#Like a string, array, range, list are sequences
#int, float is not sequence

#a=1
#print(a.__iter__)     #__iter__ is a dunder

a="gokul"
print(a.__iter__)

for i in a:
    print(i)
    print(type(i))


a=range(5)
print(a)


for i in range(5):
    print(i)

#for i in 5: ---->Error
    #print(i)


#break, continue and pass

print("aaaaaa"*4)

for i in range(5):
    if i==3:
        continue
    print(i)

for i in range(5):
    print(i)
    if i==3:
        continue

for i in range(5):
    print(i)
    if i==3:
        break

for i in range(5):
    print(i)
    i=100
    print(i)

a=1
print(a)
del a  #Deleted a from memory
#print(a)---> Error

for i in range(5):
    print(i)
    del i

for i in [0,1,2,3,4]:
    print(i) #i=0
    i=100    #i=100
    print(i) #i=100


if True:                       
    #I don't know what to do        #Can't have empty blocks in python, atleast one line should be given
 print("rest of the code")

if True:                        
    #I don't know what to do'''   #This Proves That triple quotes is not a comment
 print("rest of the code")

if True:                        
    pass                            #It is an empty statement, use to create empty block in python
print("rest of the code")


for i in range(5):
    print(i)
else:                               #This else binds to the for statement 
    print("something")              #Executes once the for loop ends



for i in range(5):
    if i==3:
        break
    else:
        print(i)
else:                               #If the for loop is ended then the else loop doesn't execute 
    print("something") 

145  
#class8-Control Flow(Problem Solving)-CipherSchools.
#Cases

n=5
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()
n=5
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()
n=5
for i in range(n):
    for j in range(n):          #It gives distance from bottom most wall 
        print(n-i,end=" ")
    print()
n=5
for i in range(n):
    for j in range(n):          #It gives distance from top most wall
        print(i+1,end=" ")
    print()
n=5
for i in range(n):
    for j in range(n):           #It gives distance from right most wall
        print(n-j,end=" ")
    print()
n=5
for i in range(n):
    for j in range(n):           #It gives distance from left most wall
        print(j+1,end=" ")
    print()

print(max(1,2,3,4,5,6,7))


n=int(input())
for i in range(n):
    for j in range(n):
        print(max(i+1,j+1,n-i,n-j),end=" ")
    print()

n=int(input())
for i in range(n):
    for j in range(n):
        print(max(i+1,j+1),max(n-i,n-j),end=" ")
    print()



n=int(input())
for i in range(n):
    for j in range(n):
        print(max(i,j),end=" ")
    print()
 

n=int(input())
for i in range(n):
    for j in range(n):
        print(max(n-j-i,n-i-1),end=" ")
    print()
