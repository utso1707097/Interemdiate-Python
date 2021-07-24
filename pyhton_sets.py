#Sets : unordered,mutable,no duplication
myset={1,2,3}
print(myset)
myset={1,2,3,1,2,1}
print(myset)
#That will be sorted
myset={5,4,2,1}
print(myset)
set1=set("Hello")
print(set1)
#To create a empty set
myset={} #Wrong this is an empty dictionary
myset=set()


#Add or remove elements
myset.add(1)
myset.add(5)
myset.add("utso")
print(myset)
myset.remove(5)
myset.discard("utso")
myset.discard("Lulu") #No error
print(myset.pop())
print(myset)
myset.clear() #empty the set

#Iterate over a set
myset={1,2,3,4,5,6}
for item in myset:
    print(f"this is {item}")

#Check if an element is in the set
if 1 in myset:
    print("yes 1 is here")

#Union & Intersection & Difference
odds={1,3,5,7,9}
evens={0,2,4,6,8}
primes={2,3,5,7}
u = odds.union(evens)
print(u)
i = odds.intersection(primes)
print(i)
diff=odds.difference(primes)
print(diff)
diff=primes.difference(odds)
print(diff)
#Symmetric difference method
#Prints a and b but not (a intersection b) or not the common elements
print(primes.symmetric_difference(odds))

#Modifying our sets
setA={1,2,3,4,5,6,7,8,9}
setB={1,2,3,10,11,12}
setA.update(setB)
print(setA) #setA is changed
#there is also a intersection update method
setA={1,2,3,4,5,6,7,8,9}
setA.intersection_update(setB) #keeping only the elements that are in both set
print(setA)
#difference update
setA={1,2,3,4,5,6,7,8,9}
setA.difference_update(setB)
print(setA)
#Symmetric_difference_update
setA={1,2,3,4,5,6,7,8,9}
setA.symmetric_difference_update(setB)
print(setA) #Common gula bad a sob update hobe

#Check if a set is a superset/subset of another set or not
setA={1,2,3,4,5,6}
setB={1,2,3}
print(setA.issubset(setB))#False
print(setB.issubset(setA))#True
print(setA.issuperset(setB))#True

#We can check if a set is disjoint of another set or no common element between them
setA={1,2,3,4,5,6}
setB={7,8,9}
print(setA.isdisjoint(setB)) #True because no common elements

#Copy two sets
setA={1,2,3}
setB=setA #If we change in setB setA also get modified
setB.add(4)
print(setA)
#We can use copy method to ignore this
setB=setA.copy()
setB.add(7)
print(setA)
print(setB)
#We can also use the set method to copy a set
setB=set(setA)

#Frozen set:Immutable set using frozenset() method
a=frozenset([1,2,3,4])
print(a)
#a.add(2)#error
#a.remove(1)#error
#But union intersection difference will not through error