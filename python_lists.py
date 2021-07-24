#Lists : ordered ,mutable , allows duplicate element
mylist=["banana","apple","cherry"]
print(mylist)
#You can add any kind of element in a list
mylist1=["banana",2,4,5.8,"banana"]
item=mylist[0] #allows duplicate element
print(item)
print(mylist[-1]) #last element
for item in mylist:
    print(f"I eat {item}")

#Check if an element is in the list
if "lemon" in mylist:
    print("yes lemon is inside the list")
else:
    print("sorry lemon")

print(len(mylist))
#To append an element to the last
mylist.append("lemon")
print(mylist)

#Insert an element at a given index
mylist.insert(1,"pineapple")
print(mylist)

#Remove the last item 
item=mylist.pop()
print(mylist)
print(item)

#Remove a specific element
item=mylist.remove("apple")
print(item)
print(mylist)

#Remove all elements from a list
mylist.clear()
print(mylist)
#Reverse a list
mylist=["apple","banana","cherry"]
mylist.reverse()
print(mylist)

#sort a list and change the array
mylist.sort()
print(mylist)

#Sort the list and don't want to change the list
ls=[1,4,5,3,2]
newls=sorted(ls)
print(ls) #The list is unchanged
print(newls)

#List with 5 zeroes
mylist =[0]*5
print(mylist)

#We can add two list by using + operate
print(mylist+ls)

#List slicing
print(ls[1:4])
print(ls[:3]) # 3,4,5 element
print(ls[2:])
#list[1:5:2] start:end:2
print(ls[::2]) #every second element
print(ls[::-1]) # another effective way to reverse the list

#Copy a list
list_org=['banana','cherry','apple']
list_copy=list_org
print(list_copy)
list_copy.reverse()
print(list_copy)
list_copy.append("lemon")
print(list_org) #See the orginal list is also changed
#Use .copy() method then the change will not happen
list_copy=list_org.copy()
#This will also work and don't change the original copy
list_copy=list_org[:]

#List comprehension
a=[1,2,3,4,5,6]
b=[i*i for i in a] #Create a new list expression in one line in this case this is a squared list of a
print(b)
