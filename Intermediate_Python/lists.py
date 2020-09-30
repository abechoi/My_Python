# lists
mylist = ["banana", "cherry", "apple"]
print(mylist)
item = mylist[-2]
print(item) # => cherry
# forloop
for i in mylist:
  print(i)
# if statement
if "lemon" in mylist:
  print("yes")
else:
  print("no")
# len()
print(len(mylist))
# append()
mylist.append("lemon")
print(mylist)
# insert() - arg1 = position, arg2 = value
mylist.insert(1, "blueberry")
print(mylist)
# pop() - removes and returns last item
item = mylist.pop()
print(item)
# clear() - removes all
# item = mylist
# print(item.clear())
# reverse()
#item = mylist.reverse()
item = mylist.reverse()
print(mylist)
# sort()
mylist = [4,2,6,1,9]
#mylist.sort()
sorted_list = sorted(mylist)
print(mylist)
# [0] * 4 = [0, 0, 0, 0]
mylist = [0] * 4
print(mylist)
# concatenate
mylist = [1,2,3,4,5]
new_list = mylist + mylist
print(new_list)
# slice()
a = mylist[-3:]
print(a) # => [3, 4, 5]; from -3 position to end
# every 2 elements
a = mylist[::2]
print(a)
# reverses list
a = mylist[::-2]
print(a)
# copy() - creates copy to same pointer, expect mutation
mylist = ["banana", "cherry", "apple"]
list_copy = mylist.copy() # prevents mutation on original list
#list_copy = mylist[:]    # also copies
#list_copy = list(mylist) # also copies
list_copy.append("lemon")
print(mylist)
# square each element
mylist = [1,2,3,4,5,6]
b = [i * i for i in mylist] # i * i = element * element
print(b)