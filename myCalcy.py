#### Write a program to do arthematic operations based on user input #####

print('Hey there! I am Calcy, I can do any arthematic operations in a split of second! What\'s your name ?')
myName = input() # Taking the user name

print('Hello, ' , myName + " What can I do for you today ?")

#Giving hints to the user 
print("Hints: Type 'Add' --> Addition, Type 'Mul' --> Multiplication, Type 'Div' -->  Division")
print("Type 'Fdiv' --> Floor Division, Type 'Exp' --> Exponential, Type 'Sub' --> Subtraction")
print("Type 'Rem' --> Remainder/modulus")
myOp = input()

## Addition
if myOp == "Add":
  print("Sure. Give me the first number ")
  myFirst = int(input())
  print("And now Give me the Second number ")
  mySecond = int(input())
  print("Processing... Please wait..")
  print("On Adding both the numbers we get = ", str(myFirst + mySecond))

## Subtraction
elif myOp == "Sub":
   print("Sure. Give me the first number ")
   myFirst = input()
   print("And now Give me the Second number ")
   mySecond = input()
   print("Processing... Please wait..")
   print("On Subtracting both the numbers we get = ", str(int(myFirst) - int(mySecond)))

## Multiplication
elif myOp == "Mul":
  print("Sure. Give me the first number ")
  myFirst = input()
  print("And now Give me the Second number ")
  mySecond = input()
  print("Processing... Please wait..")
  print("On Multiplying both the numbers we get = ", str(int(myFirst) * int(mySecond)))

## Division
elif myOp == "Div":
  print("Sure. Give me the first number ")
  myFirst = int(input())
  print("And now Give me the Second number ")
  mySecond = int(input())
  print("Processing... Please wait..")
  print("On Dividing both the numbers we get = ", str(myFirst / mySecond))

## Remainder
elif myOp == "Rem":
  print("Sure. Give me the first number ")
  myFirst = input()
  print("And now Give me the Second number ")
  mySecond = input()
  print("Processing... Please wait..")
  print("The Remainder for both the numbers is = ", str(int(myFirst) % int(mySecond)))

## Exponential
elif myOp == "Exp":
  print("Sure. Give me the first number ")
  myFirst = input()
  print("And now Give me the Second number ")
  mySecond = input()
  print("Processing... Please wait..")
  print("The exponential result is = ", str(int(myFirst) ** int(mySecond)))

## Floor Division
elif myOp == "Fdiv":
  print("Sure. Give me the first number ")
  myFirst = input()
  print("And now Give me the Second number ")
  mySecond = input()
  print("Processing... Please wait..")
  print("On performing Floor Division on both the numbers we get = ", str(int(myFirst) // int(mySecond)))

else:
  print("Sorry, I did not get that. Please refer the hints and try again")

print("Do you need anything else ?")
myCom = input()
if myCom == "No, Thank you. You are great!":
  print("Awww.. That's so nice of you. Have a great day!")

elif myCom == "Yes":
  print("Sure. Please use the below hints")
  print("Hints: Type 'Add' --> Addition, Type 'Mul' --> Multiplication, Type 'Div' -->  Division")
  print("Type 'Fdiv' --> Floor Division, Type 'Exp' --> Exponential, Type 'Sub' --> Subtraction")
  print("Type 'Rem' --> Remainder/modulus")

else:
  print("Sorry, I don't know what you meant. Please try again later")
