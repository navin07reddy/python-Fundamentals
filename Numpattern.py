# #1 reverse inverted number pattern
# n = int(input("Enter the number: "))

# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

# print("Reverse Inverted Number Pattern")

# #2 right nngle number triangle
# n = int(input("Enter the number: "))

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()


# #3 left number triangle
# n = int(input("Enter the number: "))

# for i in range(1, n+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

# print("Left Angle Number Triangle")

# #4 square number pattern
# row = int(input("Enter rows: "))
# colu = int(input("Enter columns: "))

# for i in range(row):
#     for j in range(1, colu+1):
#         print(j, end="")
#     print()

# #5 number pyramid Pattern
# rows = int(input("Enter the number: "))

# for i in range(1, rows+1):
#     for j in range(rows-i):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print(j, end="")
#     print()


# # num pattern2
# n = int(input("Enter the number: "))

# for i in range(1, n+1):

#     # spaces for pyramid shape
#     for s in range(n-i):
#         print(" ", end="")

#     # numbers
#     for j in range(1, i+1):
#         if j == 1 or j == i:
#             print(1, end=" ")
#         else:
#             print(i-1, end=" ")

#     print()

# #6 alphabets pattern traingle
# n = int(input("Enter the number: "))

# for i in range(1, n+1):

#     for s in range(n-i):
#         print(" ", end="")

#     for j in range(i):
#         print(chr(65 + j), end=" ")

#     print()


n=int(input("enter the number of rows"))
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num, end=" ")
        num=num+1
    print()
