#lambda arguments:expression
add10 = lambda x:x+10 #add10 is a function
print(add10(5))
#lambda function can have multiple arguments
mult=lambda x,y:x*y;
print(mult(10,5))

points2D=[(1,2),(15,1),(5,-1),(10,4)]
points2D_sorted=sorted(points2D)
print(points2D_sorted)
#Also we can add a key that is a function that puts the sort condition.   key=function
points2D_sorted=sorted(points2D,key=lambda x:x[1])#Sorted according to y index
print(points2D_sorted)
points2D_sorted=sorted(points2D,key=lambda x:x[0]+x[1])
print(points2D_sorted)

#map(function,sequence)
a=[1,2,3,4,5]
b=map(lambda x:x*2,a)
print(list(b))
#this can be implemented using list comrehension also
c=[x*2 for x in a]
print(c)

#filter function
#filter(function,sequence) 
#the function returns true or false
#true elements are returned
a=[2,3,6,8,11]
c=filter(lambda x:x%2==0 ,a)
print(list(c))#Returns even numbers
#this can also be done using list comprehension
d=[x for x in a if x%2==0]
print(d)

#reduce function
#reduce(function,sequence)
#returns a single value
from functools import reduce
a=[1,2,3,4,5,6]
product_a=reduce(lambda x,y:x*y,a)
print(product_a)

