# When we execute a print statement, by default a new line is inserted to after the execution.
# In order to avoid this we use 'end=' parameter
# end= is considered as a keyword arguments
# Benefits of end parameters:
 # 1. We can change the default behavior of the print statement to insert a new line after its execution.
 # 2. We can add multiple new lines to the print statement.


### Syntax
print(end="") # We insert new lines \n or character inside the double quotes. #

### Eg1: end parameter with no space and no new line
print("py", end="")
print("thon")

### Eg:2 end paramenter with a space and no new line
print("This is a tutorial on", end=" ")
print("end parameter")

### Eg:3 end parameter with a space, a comma and no new line
print("Hello", end=" ,")
print("Programmer")

### Eg:4 end parameter with mutliple lines
print("Hey", end = "!\n\n")
print("What's up with you", end = "?\n\n\n")
print("Great to see you learning Python", end= "!!\n\n\n\n")

### Eg:5 end paramete with strings and new lines inside inside
print("H",end="ey! \n\n")
print("W",end="hat's up with you? \n\n\n")
print("G",end="reat to see you learning python!! \n\n\n\n")

### Eg:6 end parameters with full strings
print(end = "Hey!\n\n")
print(end = "What's up with you?\n\n\n")
print(end = "Great to see you learning Python\n\n\n\n")

### Eg:7 end parameters with lists
nums = [1,2,3,4,5]
for i in nums:
  print(i,end="")

### Eg:8 end parameters with interactive outputs/ to receive the input in the same line
print("\nEnter Something:", end="")
val = input()
print("You've entered:", val)


# Refer this article for more info: https://codescracker.com/python/python-end.htm