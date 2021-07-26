#Errors and Exceptions
#If a code is syntactically correct but shows error when it is executed this is called exception error
#a=5 +'10' #Type error
#import somemodule #import error
#a=5 then b=c+a #name error
#f=open('somefile.txt) #File not found error if no such file in the directory
#a=[1,2,3] a.remove(4) #value error
#a=[1,2,4] print(a[4]) #index error
#mydict={'name':'Max'} print(mydict['age']) #key error

#Raising an error

x=-5
#if x>0 no exception occour
'''
if x<0:
    raise Exception('x should be positive')
'''
#assert statement: we can also do this by assert statement
'''
assert(x>=0),'x is not positive'
'''
#if x is poistive no assertion error

#handle/catch exception using try except block

'''
try:
    a=5/0
except:
    print('an error happened')
'''
#we can also catch the type of exception
'''
try:
    a=5/0
except Exception as e:
    print(e) #prints division by zero
'''
#We can write multiple statement in try block

try:
    a=5/1
    b=a+'10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
#We can also write a else clause in try except
else:
    print("Everything is fine")
#we can also write finally block.Exception occoured or not this will always runs
finally:
    print('Cleaning up')


#Define our own exception
class ValueTooHighError(Exception):
    pass
#also you can exception class this way
class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value=value

def test_value(x):
    if x>100:
        raise ValueTooHighError('value is too high')
    if x<5:
        raise ValueTooSmallError('value is too small',x)
#test_value(200)

#We can also use try and except
try:
    #test_value(200)
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message,e.value)
