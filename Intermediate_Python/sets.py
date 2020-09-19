# Sets: unordered, mutable, no duplicates
mySet = {1, 2, 3, 2, 3}
print(mySet) # => {1, 2, 3}
mySet = set([1, 2, 3])
print(mySet)
# add() adds a new element
mySet.add(4)
mySet.add(5)
# remove() removes an element, throws error if arg not found
mySet.remove(5) 
# discard() removes an element, does not throw error if arg not found
mySet.discard(4)
print(mySet)
# pop() removes first element in a set
mySet.pop()
# clear() empties a set
# mySet.clear()
mySet.add(1)
print(mySet)

for i in mySet:
  print(i)
if 1 in mySet:
  print("YES")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
# union() combines 2 sets without dupes
u = odds.union(evens)
print(u)
# intersection() returns dupes within 2 sets
i = odds.intersection(primes)
print(i) # => {3, 5, 7}

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
# difference() returns the difference in 2 sets
diff = setA.difference(setB)
print(diff)  # => {4, 5, 6, 7, 8, 9}
# symmetric_difference() returns the unique elements in 2 sets
diff = setB.symmetric_difference(setA)
print(diff) # => {4, 5, 6, 7, 8, 9, 10, 11, 12}
# update() combines unique elements within 2 sets
setA.update(setB)
print(setA)
# intersection_update() returns a set of common elements
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.intersection_update(setB)
print(setA)
# difference_update() removes commons elements on setA only
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.difference_update(setB)
print(setA)
# symmetric_difference()
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
# symmetric_difference_update() filters out the common elements from 2 sets, returns the 2 sets combined
setA.symmetric_difference_update(setB)
print(setA)
# issubset() checks if a set matches completely with the argument set
print(setA.issubset(setB))
# issuperset() checks if an argument set matches completely with a set
print(setA.issuperset(setB))
# isdisjoint() returns true if 2 sets are unique
print(setA.isdisjoint(setB))
# copy() copies a set into another
setB = setA.copy()
setB = set(setA)
# frozenset() is an immutable set
a = frozenset([1, 2, 3, 4])
print(a)