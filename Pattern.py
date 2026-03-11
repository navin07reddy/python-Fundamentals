#Reverse Inverted Star Pattern
n=int(input("enter the number"))
for i in range(5,n,-1) :   #step function
     print("*" * i)
print("Reverse Inverted Star Pattern")


#right angle triangle
n=int(input("enter the number"))
for i in range(1,n) :   
    print("*" * i)
print("ends")
print("right angle triangle")

#left traingle pattern
n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range (i):
        print("*", end="")
    print()
print("Ends")
print("left angle triangle")
  
            
 #square pattern
row=int(input("enter the number"))
colu=int(input("enter the number"))
for i in range (row):
    for j in range (colu):
        print("*",end="")
    print()

#pyramid pattern
rows = int(input("enter the number"))

for i in range(1, rows+1):
    for j in range(rows-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()

#diamond pattern 

rows = int(input("enter the number"))

for i in range(1, rows+1):
    for j in range(rows-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()
for i in range(5,0,-1):
    for j in range(rows-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()

#Butterfly wing shape
rows = int(input("enter the number"))
# Upper part
for i in range(1, rows+1):
    for j in range(i):
        print("*", end="")
    for j in range(2*(rows-i)): #to print the spaces that how much you needed
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# Lower part
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    for j in range(2*(rows-i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()


#hollow square pattern

n=int(input("enter the number"))
for i in range (n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 :
            print("*", end="")
        else:
            print(" ", end="")
    print()

