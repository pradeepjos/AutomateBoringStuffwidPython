# Chapter 2 Flow Control

# A flowchart is a logical representation of how a task would be completed. 
# To represent true or false / 1 or 0 / yes or no we use boolean operators, boolean values and comparison operators

# Boolean data type has only two values True and False

spam = True
print(spam)

# Comparison operators: 6 comparison operators. Expressions with comparison operators evaluate to Boolean
# == -> equal to
# != -> not equal to
# > -> greater than
# < -> less than
# <= -> less than equal to
# >= -> greater than equal to

# try it on the python shell
# 23 == 32 
# 43 != 45
# 24 == "24" # int will never be equal to string
# 43 == 43.0 # float can be equal to int


# Boolean operators: and, or, not
# true only when both the expressions are true, else false
#########################
#####AND Truth Table#####
#T T T
#T F F
#F F F
#F T T

print(True and True)

# OR
# T T T
# T F T
# F F F
# F T T

print(True or False)

# NOT
# T F
# F T
print(not True)


###
myAge = 26
myPet = 'Cat'
print(myAge == 26 and myAge == 'DOG')


## Summary
# 1. Boolean data type has only 2 values "True" and "False".
# 2. There are six comparision operators.
# 3. Boolean operators are and not and or