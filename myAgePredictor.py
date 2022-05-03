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
