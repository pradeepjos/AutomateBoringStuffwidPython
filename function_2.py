# creating your own functions
#  function is a mini program inside a program
#  helps us to avoid copying code

def hello():
  print("howdy")
  print("heelo")
  print("helllllllooooooooooooooooooooooooooooo\n")


hello()
hello()
hello()

# function with parameters

def hello(name):
  print("hello, " + name)


name = input()
hello(name)

# argument: value that is passed to the function call
# parameter: variable inside the function

def place(place): # variable inside the function
  print("This is ", place)

place("sparta") ## sparta here is called argument. It is the value passed to the functionc call

# return statements
def plusOne(number):
  return number + 1

newNumber = plusOne(10)
print(newNumber)

# sometimes functions return nothing.. It is called none. for example the print function. None is the only value for its data type.

spam  = print()
print(spam) # prints None

print(spam == None) # prints true

# Summary:
# Functions are like a mini-program inside your program
# the main point of function is to get rid of duplicate code.
# the def statement defines a function.
# the input to functions are arguments. The output is the return value.
# The parameters are the variables in between the function's parantheses in def statement
# the return value is specified using the return statment
# every function has a retrn value. if your function doesn't have a return statment, the default return value is  None.
# Keyword arguments to functions are usualy for optional arguments. The print() function has keyword arguments end and sep
