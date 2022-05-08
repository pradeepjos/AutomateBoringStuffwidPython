# if
# python code visualizer https://pythontutor.com/visualize.html#mode=edit
# identation is important. It visually tells us which code belongs to which block.

myName = "Pradeep"
if myName == "Pradeep":
  print("Hello, ", myName, sep = "")
print("it's done!")

## if-else

password = "swordfish"
if password == "swordfish":
  print("Welcome, back ", myName, sep = "-> ")

else:
  print("bad password. try again")

print("Its Done")

## if-elif

myName = "lice"
myAge = 3000
if myName == "Alice":
  print("Hi, ", myName)

elif myAge < 12:
  print("Who r ya")

elif myAge < 1000:
  print("Zombie")

elif myAge >= 3000:
  print("God?")

print("its done")


## truthy and false
#print("Enter your name: ")
myName = input()
if myName:
  print("Hey there!!", myName)
else:
  print("Kuch toh bolo yaar")

#bool function
print(bool(43)) # True
print(bool(0)) # false
print(bool('')) # empty char. false
print(bool("string")) # true
print(bool(0.0)) # false
print(bool(4.5)) # True

# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

spam = int(input())
if spam == 1:
  print("Hello")

elif spam == 2:
  print("Howdy")

else:
  print("Greetings!")
  



##Summary
# 1.if, if-else, elif
# 2. truthy if name:
# 3 bool function

