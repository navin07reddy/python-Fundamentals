#list data type
list1=[10,12,15,20,45,30,32]
list2=["naveenkumar"]
print(list1)  
print(list1[0:4]) #slicing 
list1.append(53) # by using append method u can add the element at the end automatically
print(list1)
list1.insert(3,45) # inserting the element at the specific position 
print(list1)
list1.remove(30)
print(list1) #after removing 30 from the list
list1.pop()
print(list1)
#a= list2[0][0:5] #  string slicing
#print(a)
b= list2[0][::-2]  
print(b)
print(len(list1))

#tuple: this  are used to store the multiple in a single variable (ordered and unchangebale)

tuple1= ("banana", "appple", "apple","kiwi")
print(tuple1[0])    # accessing an element from the tuple
y=list(tuple1)
y[1]="orange"
y.append("grap") 
tuple1 = tuple(y)
print(tuple1)   # to change order or update the values into tuple we first convert it into list and then convert it into tuple 

#Dictionary
# Dictionaries are used to store data values in key:value pairs and we store inside curly braces
# dictionary is a collection which is ordered, changeable and do not allow duplicates
dict1 = {
  "name": "naveen",
  "middle name": "kumar",
  "age": 23
}
print(dict1)
print(dict1["name"]) # we can access by key value

dict1["age"]=24 # we can change specific item by using its key name
print(dict1)
dict1.pop("name")
print(dict1)