import json
person={'name':'utso','age':20,'city':'Chuadanga','haschild':False,'titles':['Engineer','Scientist','Programmer']}
#Python to json format ->(Serialization or encoding)
#dumps for converting python object to a json string
personJSON=json.dumps(person,indent=4,sort_keys=True)
print(personJSON)

#Write a json file from python
#dump for converting a python object to a json file
with open('person.json','w') as file:
    json.dump(person,file,indent=4)

#Deserialization or decoding ->(json to python)
#loads for decoding from a string
person=json.loads(personJSON)
print(person)

#Convert from a json file 
#load for decoding from a json file
with open('person.json','r') as file:
    person=json.load(file)
    print(person)

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

user=User('Utso',24)
#userJSON = json.dumps(user) #Error: we have to write custom encoding function to make Object of type User JSON serializable
def encode_user(obj):
    if isinstance(obj,User):
        return {'name':obj.name,'age':obj.age,obj.__class__.__name__:True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

userJSON=json.dumps(user,default=encode_user,indent=4)
print(userJSON)
#There is also another way we can implement a custom json encoder

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self,obj):
        if isinstance(obj,User):
            return {'name':obj.name,'age':obj.age,obj.__class__.__name__:True}
        return JSONEncoder.default(self,obj)

userJSON=json.dumps(user,cls=UserEncoder,indent=4)
print(userJSON)
userJSON=UserEncoder().encode(user)
print(userJSON)

#JSON to object 
user=json.loads(userJSON)
print(user)
print(type(user)) #dictionary not an object

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'],age=dct['age'])
    return dct
user=json.loads(userJSON,object_hook=decode_user)
print(user.name)
print(type(user)) #Thisis an object of User class