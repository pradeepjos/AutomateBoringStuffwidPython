# This program says hello and asks for my name
# Python executes instructions from the top. 
# Functions are like mini programs

print("Hello World!")
print("What is your name?") # ask for their name

myName = input()
print("It is good to meet you, " + myName)
print("The length of you name is: ")
print(len(myName)) # calculates the length of the name
print('What is your age?') #ask for their age

myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')


print(len('Pradeep') * 10)
print(len('Pradeep') + 1)

## data type conversions
print(int('1234'))
print(str(23))
print(float('3.14'))


## Summary:
# 1. Type programs into file editor
# 2. The execution starts at the top and moves to the bottom
# 3. # Comments are ignored
# 4. Functions are like mini programs.
# 5. print() displays the value passed to it
# 6. input () lets user type in a value
# 7. len() takes a string value and return an integer value of the string's length
# 8. int(), str(), float() convert values'data type

# Refer this amazing article on end paramenters https://codescracker.com/python/python-end.htm#:~:text=The%20end%20%28end%3D%29%20can%20be%20seen%20in%20many,%28%29%20automatically%20inserts%20a%20newline%20after%20each%20execution.