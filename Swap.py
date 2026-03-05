#1: swap two numbers
a=10
b=20
print("before swapping")
print(a,b)
a,b=b,a #swapping 
print("after swap")
print(a,b)

#2 : user input variables
name=input("enter the name")  #string input
age=int(input("enter the age"))   #integer input
salary=float(input("enter the salary"))   #float input
print( "name:", name)
print( "age:", age)
print( "salary:", salary)

#3: Checking the data type

a = 100             
b = 25.5             
c = "naveen"       
d = True           #Boolean value

#Checking and printing the data type of each variable
print("Value of a:", a)
print("Data type of a:", type(a))   # Shows type of integer
print("Value of b:", b)
print("Data type of b:", type(b))   # Shows type of float
print("Value of c:", c)
print("Data type of c:", type(c))   # Shows type of string
print("Value of d:", d)
print("Data type of d:", type(d))   # Shows type of boolean

#4: Type conversion
a= 100      #manual conversion 
b= float(a)
print (type(b))
 
a=100     # Implicit coversion
b=4.5
c= a+b  # int auto coverts to float
print(type(c))

#5: simple calculator
#user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#operator input
operator = input("Enter operator (+, -, *, /): ")

#Performing calculation
if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Division by zero is not allowed.")

else:
    print("Invalid operator!")



#6: create list and print

list1 = [10, 25.5, "Naveen", False, [1, 2, 3]]

#Printing the complete list
print("Complete List:", list1)

#7: Creating a tuple and find index and count 

tuple1=(10, 20, 30, 20, 40, 20)

print("Tuple:", tuple1)  # Printing the tuple

index_value = tuple1.index(20)   # Finding index of element 20
print("Index of 20:", index_value)

count_value = tuple1.count(20)      # Counting how many times 20 appears
print("Count of 20:", count_value)




