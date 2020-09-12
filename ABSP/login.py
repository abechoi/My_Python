myFile = open('secretFile.txt')
secret = myFile.read()
print("enter password:")
password = input()

if password == secret:
  print("access granted!")
  if password == "12345":
    print("weak password!")
else:
  print("access denied")