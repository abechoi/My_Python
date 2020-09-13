# PYTHON CHEATSHEET
> "When you arise in the morning, think of what a precious privilege it is to be alive
> - to breath, to think, to enjoy, to love."
> *- Marcus Aurelius*

## 1. LISTS []

1. ###### List Methods:
  1. len( arg1 ) - returns length of list
  1. append( arg1 ) - appends element
  1. insert( position, value ) - inserts value into an element's position
  1. pop() - removes and returns last element
  1. clear() - clears and mutates the list
  1. reverse() - reverses and mutates the list
  1. sort() - orders and mutates list incrementally
  1. copy() - copies list into another and prevents mutation

1. ###### List Functions:
  1. concat = list1 + list2; concatenates the lists
  1. slice = list[0:]; returns list from the 0 element to the last element
  1. slice = list[-2:]; returns the second to last element from list
  1. slice = list[::2]; returns list with every 2 elements
  1. slice = list[::-2]; returns reversed list and every 2 elements
  1. copy = list[:]; copies list into another and prevents mutation
  1. copy = list(mylist); copies list into another and prevents mutation
  1. squared = [ i * i for i in list]; returns list with squared elements ( i * i == element * element)