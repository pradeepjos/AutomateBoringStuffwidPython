#### Write a program to tell the user what their age gonna be next year ####

#Introductions
print("Hey there! I am Age Predictor. I can predict what your age will be next year. What's your name ? ")
myName = input()
print("Nice to meet you, ", myName)

# Gives the user the number of letters in their name
print("There are ", str(len(myName)) + " letters in your name")

# Ask the user for age
print("Tell me your current age")
myAge = input()

# Print the age of the user for the next year
print("Your current age is", myAge + ". Your age will be", str(int(myAge)+1) + " next year!")

print(len('Pradeep') * 10) # here the output would be 70
print(len('Pradeep') + 1) # here the output would be 8

## data type conversions
print(int('1234')) # we are converting a str into a int
print(str(23)) # we are coverting an int into a str
print(float('3.14')) # we are converting a str into a float


## Summary:
# 1. Type programs into file editor.
# 2. The execution starts at the top and moves to the bottom.
# 3. # Comments are ignored.
# 4. Functions are like mini programs.
# 5. print() displays the value passed to it.
# 6. input () lets user type in a value.
# 7. len() takes a string value and return an integer value of the string's length.
# 8. int(), str(), float() convert values'data type.

# Refer this amazing article on end paramenters: https://codescracker.com/python/python-end.htm#:~:text=The%20end%20%28end%3D%29%20can%20be%20seen%20in%20many,%28%29%20automatically%20inserts%20a%20newline%20after%20each%20execution.
