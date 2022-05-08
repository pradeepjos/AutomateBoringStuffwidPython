# while loop as long as the condition is true.
# for loop executes a specific number of times.
# print odd number between to 99

odd = 0
even = 0
for i in range(1,100):
  if i%3 == 0:
      odd = odd + 1
  else:
      even = even + 1
    
print(odd)
print(even)
print("it is done!")


# print your name 5 times
print("My name is ")
for i in range(5):
  print("Jimmy five times ", str(i))

# sum of first 100 numbers
sum = 0
for num in range(1, 101): # range functions(start, ending -1, step)
  sum = sum + num

print(sum)


#Summary
# for loop executes for specific number of times
# range function () can be called with one, two, or three arguments.
# break and continue can also be used in for loops.

