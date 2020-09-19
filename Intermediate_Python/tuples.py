# Tuple: ordered, immutable, allows dupes
# create a tuple
myTuple = ("Max", 28, "Boston")
print(myTuple)
print(type(myTuple))
notTuple = ("Max")
print(type(notTuple))

# tuple() creates a tuple
myTuple = tuple(["Max", 28, "Boston"])
item = myTuple[0]
print(item)

# myTuple[0] = "Tim"
for i in myTuple:
  print(i)

if "Tim" in myTuple:
  print("YES")
else:
  print("NO")

# count() returns number of arg1 within myTuple
# index() returns the index of the first match within myTuple
myTuple = ('a','p','p','l','e')
print(myTuple.count('p')) # => 2
print(myTuple.index('p')) # => 1

myList = list(myTuple)
print(myList)
myTuple = tuple(myList)
print(myTuple)
# slice() - arg1 = start-index, arg2 = end-index minus 1
a = (1,2,3,4,5,6,7,8,9,10)
b = a[2:5]
print(b) # => (3, 4, 5)
b = a[::-2]
print(b) # => (10, 8, 6, 4, 2)
# unpacking tuple into variables
myTuple = "Max", 28, "Boston"
name, age, city = myTuple
print(name)
print(age)
print(city)
myTuple = (0,1,2,3,4)
i1, *i2, i3 = myTuple
print(i1) # => 0
print(i2) # => [1, 2, 3]
print(i3) # => 4
# sys.getsizeof() returns byte size
import sys
myList = [0, 1, 2, "hello", True]
myTuple = (0, 1, 3, "hello", True)
print(sys.getsizeof(myList), "bytes")
print(sys.getsizeof(myTuple), "bytes")
# timeit.timeit()
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))