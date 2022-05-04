## sep parameter: you can separate multiple parameters using value assigned for it.

# Eg: print character
print("s","e","p") # the output has default spaces between each character.

# Eg: with sep
print("s", "e", "p", sep = "") # the output has no default spaces

## Benefits:
 # 1. remove default spaces
 # 2. insert required characters

# Eg:
print("My Computer", "Desktop", "Cricket07", sep = " ->")

# Eg: with espace character \b backsspace
print("s ", "e ", "p", sep="\b")

# Eg:
print("5","4","2022", sep="/")

#Eg:
val = ["1","2","3","4","5"]
for i in val:
  print(i, end = " ",  sep = "/b")
