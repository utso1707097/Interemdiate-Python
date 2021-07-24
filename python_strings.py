#String: ordered , immutable,text representation
mystring='hello world' #'' or "" quotes
print(mystring)
mystring2='I\'m utso'
#mystring2="I\'m utso"
print(mystring2)
mystring3='''Hello
mohot
utso'''
print(mystring3)

#Access index
char=mystring[-1]

#string are immutable can't be change
#mystring[2]='h'#will through an error

#slicing in string
substring=mystring[0:5]
print(substring)
substring=mystring[::-1] #Reverse the string
print(substring)

#Concatenation
greeting="Hello"
name= "Tom"
str=greeting+" "+name
print(f"{greeting} {name}")
print(str)

#Access character by character
for char in mystring:
    print(char)

#If a substring or letter in a string
if "Tom" in str:
    print("Yes I am tom")

#Remove whitespace by strip() method
mystring='    Hello world    '
print(mystring)
mystring=mystring.strip()
print(mystring)

#Upper lower
print(mystring.upper())
print(mystring.lower())

#Check if a string start/ends with a specific letter or substring
print(mystring.startswith("Hello"))
print(mystring.endswith("world"))

#Find a specific character or substring
print(mystring.find('o'))
print(mystring.find('llo'))
print(mystring.find('u')) #Retruns -1 because u is not in mystring

#Count the no of character or substring
print(mystring.count('o'))
print(mystring.count('llo'))

#Replace in a string
mystring=mystring.replace('world','universe')
print(mystring)

#List and string
#String to list
mystring='how are you doing'
mylist=mystring.split() #default split argument is space
print(mylist)
newstring="apple*alu*banana"
mylist=newstring.split("*")
print(mylist)

#List to string
newstring=' '.join(mylist)
print(newstring)
# comma die join hobe
mystring=','.join(mylist)
print(mystring)

mylist=['a']*6
print(mylist)
mystring=''.join(mylist)
print(mystring) #aaaaaa

#Formatting string
# %,format(),f-string
var1 = "Tom"
var2=22
var3=3.141592
mystring="my friend name is %s" %var1
print(mystring)
mystring="Hello {}.You are now {}".format(var1,var2)
print(mystring)
#We can also specify the no of digits after floating point
mystring="The value of PI is {:.2f}".format(var3)
print(mystring)
#New formatting style called f-string
mystring=f"Hey Mr. {var1}.See you later {var2} and {var3*5}"
print(mystring)