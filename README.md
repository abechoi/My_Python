# PYTHON CHEATSHEET
> *"When you arise in the morning, think of what a precious privilege it is to be alive - to breath, to think, to enjoy, to love."*
> *- Marcus Aurelius*

## 1. LISTS []

* **List Methods:**
  * list() - creates a list
  * len( arg1 ) - returns length of list
  * append( arg1 ) - appends element
  * insert( position, value ) - inserts value into an element's position
  * pop() - removes and returns last element
  * clear() - clears and mutates the list
  * reverse() - reverses and mutates the list
  * sort() - orders and mutates list incrementally
  * copy() - copies list into another and prevents mutation

* **List Functions:**
  * concat = list1 + list2; concatenates the lists
  * slice = list[0:]; returns list from the 0 element to the last element
  * slice = list[-2:]; returns the second to last element from list
  * slice = list[::2]; returns list with every 2 elements
  * slice = list[::-2]; returns reversed list and every 2 elements
  * copy = list[:]; copies list into another and prevents mutation
  * copy = list(mylist); copies list into another and prevents mutation
  * squared = [ i * i for i in list]; returns list with squared elements ( i * i == element * element)

## 2. TUPLES ()

* **Tuple Methods:**
  * tuple( args ) - creates a tuple
  * count( arg1 ) - returns number of matches within a tuple
  * index( arg1 ) - returns index of the first match within a tuple

## 3. DICTIONARY {}

* **Dictionary Methods:**
  * dict( args ) - creates a dictionary
  * del - removes a key within a dictionary
  * pop( arg1 ) - takes a key as an arg and removes/returns it
  * popitem() - removes and returns last item in a dictionary
  * keys() - returns keys within a dictionary
  * values() - returns values within a dictionary
  * update( arg1 ) - overwrites one dictionary with another

* **Dictionary Functions:**
  * dict1 = {tuple1: 1}; uses a tuple as a key within a dictionary

## 4. SETS {}

* **Sets Methods:**
  * set( args ) - creates a set
  * add( arg1 ) - adds element to a set
  * remove( arg1 ) - removes element, throws error if arg not found
  * discard( arg1 ) - removes element, does not throw error if arg not found
  * pop() - removes and returns a random element
  * clear() - empties a set
  * union() - combines 2 sets without dupes
  * intersection() - returns a set of dupes within 2 sets
  * difference() - returns the difference in 2 sets
  * symmetric_difference() - returns the unique elements in 2 sets
  * update() - combines unique elements within 2 sets
  * intersection_update() - returns a set of common elements
  * difference_update() - removes commons elements on setA only
  * symmetric_difference_update() - filters out the common elements from 2 sets, returns the 2 sets combined
  * issubset() - checks if a set matches completely with the argument set
  * issuperset() - checks if an argument set matches completely with a set
  * isdisjoint() - returns true if 2 sets are unique
  * copy() - copies a set into another
  * frozenset() - is an immutable set

## 5. Strings

* **String Methods**
  * strip() - removes whitespace
  * upper() - sets string as uppercase
  * lower() - sets string as lowercase
  * startswith( arg1 ) - returns True if string starts with the arg
  * endwith( arg1 ) - returns True if string ends with the arg
  * find( arg1 ) - returns index of the first match
  * count( arg1) - returns number of matches with the arg
  * replace( arg1, arg2 ) - replaces arg1 with arg2
  * split( arg1 ) - splits apart a string into a list, delimiter is a space by default
  * join( arg1 ) - converts list into a string

* **String Functions**
  * "" - creates empty string
  * """ multiline string """ - creates a multiline string, "\" removes line
  * myString[0] - returns first character
  * myString[-1] - returns last character
  * myString[:5] - returns first 5 characters
  * myString[::-1] - returns a reversed string
  * Formatting Strings (Deprecated): "Today is %s's birthday. " %var
  * Formatting Strings (Deprecated): "The variable is {:.2f} and {:4f}".format(var, pi)
  * Formatting Strings (Best Practice): f"{var} is my {relationship}"

## MODULES

* **sys**
  * sys.getsizeof( arg1 ) - returns variable's byte size

* **timeit**
  * timeit.timeit(stmt="arg1", number= arg2 )) - returns time of creation