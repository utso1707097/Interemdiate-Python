#Collection:Counter,namedtuple,OrderedDcit,defaultdict,deque

#Counter
from collections import Counter
a='aaabbccccd'#We can also have a lists
my_counter=Counter(a)
print(my_counter) #Dictionary key-value pairs
for key,value in my_counter.items():
    print (f"{key} : {value}")

#This will return list of tuples
print(my_counter.most_common(1)) #1st Most common element and times that element occours in string
print(my_counter.most_common(2)) #first two most occouring characters
#If we want to see the most common element
print(my_counter.most_common(1)[0][0]) #most common element
print(list(my_counter.elements()))

#namedtuple : easy to create light easy to create an object type simillar to a struct
from collections import namedtuple 
Point=namedtuple('Point','name,age') #This will create a class named Point with variable name and age
pt=Point('utso',22)
print(pt)
print(pt.name,pt.age)

#Ordereddict : Dictionary that remembers the order
from collections import OrderedDict
ordered_dict=OrderedDict()
ordered_dict['b']=2
ordered_dict['c']=3
ordered_dict['d']=4
ordered_dict['a']=1
print(ordered_dict)
#Now a normal dictionary remembers the order

#defalutdict :default type
from collections import defaultdict
d=defaultdict(int)
d['a']=1
d['b']=5
print(d['b'])
print(d['c']) #Print default type of integer if key is not present

#deque : Double ended queue that can insert and delete elements from both side
from collections import deque
d =deque()
d.append(1)
d.append(2) #append element to last
d.appendleft(30)#append element to the very left
print(d)
d.pop() #Return and remove the last element
print(d)
d.popleft() #Return and remove the leftmost element 
print(d)
d.clear() #Will clear the deque
print(d)
d.extend([50,60,70]) #extend the elements to the right
d.extendleft([-10,-20,-30]) #extend the elements to the left
print(d)
#We can also rotate our deque
d.rotate(1) #Rotate to right side by 1
print(d)
d.rotate(2)
print(d)
d.rotate(-3)#that rotates 3 times left
print(d)
