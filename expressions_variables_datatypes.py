# Chapter 1

# Following the course http://automatetheboringstuff.com/chapter1/ 

print(2+2) # Expressions =  values + operators; always evaluate to a single value

# Most Commonl used Operators

print("Multiplication (*)-->", 2 * 2) # Multiplication

print("Division (/) --> ", 12 / 3) # Division - returns the quotient in float (decimals)

print("Addition (+) --> ", 2 + 2) # Addition

print("Floor Division (//) --> ", 16 // 3) # Division operator but quotient is rounded off. does not return in float (decimals)

print("Exponential (**) --> ", 2 ** 3) # Exponent of a value.

print("Modulus / Remainder (%) -->", 15 % 3) # returns the reminder

print("Subtraction (-) --> ", 10 - 5) # Subtraction

# Precedence : The order of operations. 
# Paranthesis --> Exponential -- > Multiplication --> Division --> Addition --> Subtraction

print("The result of 2 + 3 * 6 is -->", 2 + 3 * 6)

print("The reuslt of (2 + 3) * 6 --> ", (2 + 3) * 6) # precedence moves from left to right

print("The result of (5-1) * ((7 + 1) / (3-1))", (5-1) * ((7 + 1) / (3-1))) # values inside the paranthesis are calculated first

# Data Types : Every value has exactly one unique data type
# Integers: negative and positive numbers;  number that cannot be written in fractions
# Floats: Decimals. Numbers that are written in fractions
# Strings: Text values. Enclosed in single or double quotations

# String concatenation: joining two strnigs

print("Alice" + ' Bob')

# we can also mulitply a string with an integer

print('Alice' * 10) 

print(("HI ") + "!" * 100)


# Variables: we can save values to computer's memory using variables.

spam = 'Hello' # stores the value; = is called assignement operator

print(spam) # prints the value inside the variable spam

print(spam + " World") # string concatenation

spam = "Goodbye" # overwriting the value inside the spam variable

print(spam + " World")

# If an expression does not evaluate to a single value it is a statement.

spam = 77

spam = spam + 4

print(spam)


## Summary:
 # 1. IDLE - Integrated Development Environment
 # 2. Interactive Shell >>> for testing simple commands
 # 3. File Editor for writing large programs
 # 4. Expressions = Values + Operator
 # 5. Precedence: PEDMAS
 # 6. Data Types = String, Float, Integers
 # 7. String concatenation, String * Integers
 # 8. Variables
 # 9. Spam + 1

### End of Chapter 1###
### Link: http://automatetheboringstuff.com/chapter1/ ###