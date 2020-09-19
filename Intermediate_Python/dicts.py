# Dictionary: key-value pairs, unordered, mutable
myDict = {"name": "Max", "age": 28, "city": "New York"}
print(myDict)
# dict() creates a dictionary
myDict = dict(name="Mary", age=27, city="Boston")
print(myDict)
# get value of the key: name
value = myDict["name"]
print(value)
# adds new key with a new value to myDict
myDict["email"] = "me@abechoi.com"
print(myDict)
# overwrites value of "email"
myDict["email"] = "mary@abechoi.com"
print(myDict)
# del - deletes name key
#del myDict["name"]
print(myDict)
# pop( arg1 ) removes key
myDict.pop("age")
print(myDict)
# poptime() removes last element in dictionary
myDict.popitem()
print(myDict)

if "name" in myDict:
  print(myDict["name"])

try:
  print(myDict["hi"])
except:
  print("error")

# keys() prints keys
for i in myDict.keys():
  print(i)
# values() prints values
for i in myDict.values():
  print(i)
for key,value in myDict.items():
  print(key, value)

# copy() copies dictionary without mutations
myDictCopy1 = myDict.copy()
myDictCopy2 = dict(myDict)

# update() overwrites a dictionary with another dictionary
originalDict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
updatedDict = dict(name="Mary", age=27, city="Boston")
originalDict.update(updatedDict)
print(originalDict)

# tuple can be used as a key
myTuple = (8,7)
myDict = {myTuple: 15}
print(myDict)