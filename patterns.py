# patterns in python 
# There are two types of patterns in python 
# 1. solid type 
# 2. hallow type 

# first we will see some solid type patterns 

# square pattern

n= int(input("enter n"))
def square(n):  # creating a function to implement this pattern
    for i in range(0,n): #outer loop
        for j in range(0,n): #iner loop 
            print("* ",end=" ") # end=" " if you dont keep this it wont print 5 stars in a line instead it will be printing one by one so thats why we written 'end=" "''
        print() # this is the line where the first row ends 

square(n)   # calling the function 


# 2 increasing traingle
n=int(input("enter n"))
def inctriangle(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print()
inctriangle(n)

# 3 decreasing triangle
n=int(input("enter n"))
def dectriangle(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print("* ",end=" ")
        print()
dectriangle(n)


#3 now will will print the pattern k so once look at the means break the letter k it seems like combination of decreasing triangle and + increasig triangle right

# so just add above two codes thats it 

# k pattern 

n=int(input("enter n"))
def kpattern(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print("* ",end=" ")
        print()
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end=" ")
        print()
kpattern(n)

# 4 now we will see how to print excat triangle 

n=int(input("enter n"))
def excat_triangle(n):
    for i in range(0,n):
        print(" "*(n-i),end=" ")
        print("* "*(i+1))
   
excat_triangle(n)

# 5 excat decreasing triangle

n= int(input("enter n"))
def excat_dec(n):
    for i in range(0,n):
        print(" "*i,end=" ")
        print("* "*(n-i))
excat_dec(n)

# 6 pattern diamond
n=int(input("enter n"))
def diamond(n):
    for i in range(0,n):
        print(" "*(n-i),end=" ")
        print("* "*(i+1))
    for i in range(0,n):
        print(" "*(i+1),end=" ")
        print("* "*(n-i))
diamond(n)
    
# crown pattern
n=int(input("enter n"))
def crown(n):
    for i in range(0,n):
        if i == n - 1:
            # Last line → full stars without gap
            print("*" * (i + 1) + "*" * (i + 1))
            
        else:
            print("*"*(i+1),end=" ")
            print(" "*(2*(n-i-2)),end=" ")
            print("*"*(i+1))
crown(n)
    
    



    
    