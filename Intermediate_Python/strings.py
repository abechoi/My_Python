# Strings: ordered, immutable, text representation
myString = "Hello World"
# use """ for multiline strings
# use \ to remove line
multilines = """
this is \
a multiline
string
"""
print(myString)
print(multilines)
# get first character from myString
char = myString[0] # => H
# get last character from myString
char = myString[-1] # => d
print(char)
# slice
substring = myString[0:5]
print(substring)
# reverse string
reverseString = myString[::-1]
print(reverseString)
# concatenate strings
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)
# print every letter in greeting
for i in greeting:
  print(i)
# find ello within greeting
if 'ello' in greeting:
  print("yes")
else:
  print("no")
# strip() removes white spaces
myString = "   Hello World   "
myString = myString.strip()
print(myString)
# upper() - sets string as uppercase
print(myString.upper())
# lower() - sets string as lowercase
print(myString.lower())
# startswith( arg1 ) - returns True if string starts with the arg
print(myString.startswith("He")) # => true
# endwith( arg1 ) - returns True if string ends with the arg
print(myString.endswith("World")) # => true
# find( arg1 ) - returns index of the first match
print(myString.find("o")) # => 4
# count( arg1) - returns number of matches with the arg
print(myString.count("o")) # => 2
# replace( arg1, arg2 ) - replaces arg1 with arg2
print(myString.replace("World", "Abe")) # => Hello Abe
# split( arg1 ) - splits apart a string into a list, delimiter is a space by default
myString = "How are you doing"
myList = myString.split(" ")
print(myList)
# join( arg1 ) - converts list into a string
newString = " ".join(myList)
print(newString)

# converting list into a string: join vs loop
from timeit import default_timer as timer
myList = ["a"] * 10

# loop (bad)
start = timer()
myString = ""
for i in myList:
  myString += i
stop = timer()
print(stop-start)

# join (good)
start = timer()
myString = "".join(myList)
stop = timer()
print(stop-start)

# Formatting Strings
# % deprecated
var = "Tommy"
myString = "Today is %s's birthday. " %var
print(myString)
# format() deprecated
age = 30
myString = "{} is {} years old today.".format(var, age)
print(myString)
var = 3.1234567
pi = 3.16093232
myString = "The variable is {:.2f} and {:4f}".format(var, pi)
print(myString)
# fstring
var = "Tommy"
relationship = "younger brother"
myString = f"{var} is my {relationship}"
print(myString)