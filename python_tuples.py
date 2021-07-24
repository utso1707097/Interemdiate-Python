#Tuple: ordered,immutable,allows duplicate elements
#We can't change tuple after creating
mytuple=("Max",28,"Boston")
#1 element tuple
tup=("utso",)
mylist=[1,2,3]
mytuple=tuple(mylist)
print(mytuple)

item=mytuple[1]
print(item)
item=mytuple[-1]
print(item)

#Item cannot be assigned
#
for item in mytuple:
    print(item)
#Check if an element in the tuple
if 2 in mytuple:
    print("Fuck You")

#Length of tuple
print(len(mytuple))

#Count how many times a specific element of a tuple
mytuple=('a','p','p','l','e')
print(mytuple.count('p'))

#first occurence of a element
print(mytuple.index('p'))
mylist=list(mytuple)
print(mylist)

#Slicing a tuple
a=(1,2,3,4,5,6,7,8,9)
b=a[2:5]
print(b)
c=a[-2:]
print(c)
#We can also specify a step in the slice
b=a[1:7:2]
print(b)

#This is a trick to reverse the tuple
b=a[::-1]
print(b)

#Unpacking the tuple
#We can define tuple without ()
my_tuple= "Utso",28,"Chuadanga"
name,age,city=my_tuple
print(f"my name is {name}.I am {age} years old.I live in {city}")

#We can also unpack multiple elements by using a *
mytuple=(1,2,3,4,5,6)
i1,i2,*i3,i4=mytuple
print(i1)#first element of the tuple
print(i4)#last element of the tuple
print(i3)#3,4,5 element and this is a list
print(type(i3))#list

#Compare a tuple and a list
#We can see that list is larger than tuple with the same element
import sys
mylist=[0,1,2,"hello",True]
mytuple=(0,1,2,"hello",True)
print(sys.getsizeof(mylist))
print(sys.getsizeof(mytuple))

#It tooks much longer time to create a list than tuple
#Tuple is more efficient than list in case of time and space
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000))#100000 times creating a list time
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=1000000))#100000 times creating a tuple time
