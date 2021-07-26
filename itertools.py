# itertools: product, permutations,combinations,accumulate,groupby,and infinite iterators
from itertools import product
a=[1,2]
b=[3]
prod=product(a,b)
print(prod)
print(list(prod))#1,3 1,4 2,3 2,4
prod=product(a,b,repeat=2) #repeat two times
print(list(prod))

#Permutation
from itertools import permutations
a=[1,2,3]
perm=permutations(a)#3p3 
print(list(perm))#Prints all number of permutations
#We can also specify the length with the permutation
a=[1,2,3,4]
perm=permutations(a,2) #4p2 here 2 is length
print(list(perm))

#Combination
from itertools import combinations,combinations_with_replacement,accumulate
comb=combinations(a,2)#Length is mandatory here
print(list(comb))

comb_wr=combinations_with_replacement(a,2)
print(list(comb_wr))

a=[1,2,3,4]
acc=accumulate(a)
print(a)
print(list(acc))#print accumulated sum

import operator
acc=accumulate(a,func=operator.mul)#print accumulated max
print(list(acc))

a=[1,2,5,4,6,2]
acc=accumulate(a,func=max)
print(list(acc))

#group by
def smaller_than_3(x):
    return x<3
from itertools import groupby,count,cycle,repeat
a=[1,2,3,4]
group_by=groupby(a,key=smaller_than_3)
for key,value in group_by:
    print(key,list(value))
#Same thing for lambda function
group_obj=groupby(a,key=lambda x: x<3)
for key,value in group_obj:
    print(key,list(value))
persons=[{'name':'Tim','age':25},{'name':'Dan','age':23},{'name':'Tissa','age':23},{'name':'Cherry','age':22}]
group_obj=groupby(persons,key=lambda x:x['age'])
for key,value in group_obj:
    print(key,list(value))

for i in count(10):
    print(i) #10 to infinity
    if(i==15):
        break

a=[1,2,3]
b=0
for i in cycle(a):
    print(i) #1,2,3 is printed in a cycle
    b+=1
    if b==15:
        break

#for i in repeat(1): infinite loop
for i in repeat(1,10):
    print(i)#prints 1 10 times