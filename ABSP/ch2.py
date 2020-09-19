# 9. Write code that prints Hello if 1 is stored in spam,
# prints Howdy if 2 is stored in spam, and prints Greetings!,
# if anything else is stored in spam.
print("Enter a number:")
spam = int(input())
if spam == 1:
  print("Hello")
elif spam == 2:
  print("Howdy")
else:
  print("Greetings!")

# 13. Write a short program that prints the numbers 1 to 10 
# using a for loop, then write a program that prints 1 to 10 
# using a while loop.
for i in range(1, 11):
  print(i)
i = 1
while i < 11:
  print(i)
  i += 1