#Dictionary: key-value pairs,Unordered,Mutable

mydict={"name":"utso","age":28,"city":"Newyork"}
print(mydict)
#We can also use dict keyword to create a dictionary
#You don't have to use quotes for keys in dict method
mydict=dict(name="utso",age=25,city="Newyork")
print(mydict)

#Access the values
value=mydict["name"]
print(value)

#Add and change item in dictionary
mydict["gender"]="male"
print(mydict)
mydict["name"]="Mithila"
print(mydict)

#Delete a element
del mydict["name"]
print(mydict)
mydict.pop("age")
print(mydict)
mydict.popitem()#This removes the last element
print(mydict)

#You can check if a key is inside a dictionary or not
if "city" in mydict:
    print(mydict["city"])
#Or you can use exception handling method to check if an element is present or not
try:
    print(mydict["name"])
except:
    print("Oh bitch that key is not present")

try:
    print(mydict["city"])
except:
    print("Oh bitch that key is not present")

#Loop through a dictionary
#loop over the keys
mydict=dict(name="mithila",age=25,city="Bagerhat")
for key in mydict:
    print(key)
for key in mydict.keys():
    print(key)
#Loop over the values
for value in mydict.values():
    print(value)
#Loop over the key and values both
for key,value in mydict.items():
    print(key,value)

#Copy a dictionary
mydict_cpy=mydict
print(mydict_cpy)
#Now if we modify the copy that also modify the original
mydict_cpy["email"]="utso1707097@gmail.com"
print(mydict_cpy)
print(mydict)
#So you should use copy function
mydict_cpy=mydict.copy()
mydict_cpy["gender"]="female"
print(mydict)
print(mydict_cpy)
#We can also create a copy using dict() function then original copy will be not affected
mydict_cpy=dict(mydict)

#Merge two dictionary update() method
dict1={"name":"utso","age":22,"email":"utso707097@gmail.com"}
dict2={"name":"Max","age":24,"city":"Chuadanga"}
dict1.update(dict2)
print(dict1)

#Dictionary of numbers
mydict={3:9,6:36,9:81}
print(mydict)
#print(mydict[0])#will raise an error
print(mydict[3])

#We can use tuple in dictionary but can't use list because list is mutable
mytuple=8,7
mydict={mytuple:15}
print(mydict)