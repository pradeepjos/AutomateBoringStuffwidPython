# while loop
# differnce between a while and if is that if condition breaks once the logic is satisfied/not satisfied. Where as while loop runs till the logic is satisfied.

# input validation
# 
from pydoc import doc


print("Please enter your name")
name = input()
while name == '':
  print('Sorry, we did not get you. Please try again')
  name = input()
print("done")

# break and continue
print("please enter a number:")
num1 = int(input())
while num1:
  print("Thank you for entering a value. We are evaluating it. Please wait")
  if num1 < 0:
    print("please provide a valid number")
    num1 = int(input())
    continue
  else:
    break
print("that's how its done! You've entered :", end = str(num1))


# when a continue statement is used
spam = 1
while spam:
    spam = spam + 1
    if spam == 10:
        continue
    elif spam == 12:
        print("You have just reached 12")
        break
    print("spam is now", str(spam))
print("toasted!")

# while loop print name 5 times

name = "pradeep"
num = 0
while name != '':
  num = num + 1
  print("pradeep 5 times ", str(num))
  if num == 5:
    break
  else:
    continue

# Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# for loop
for i in range(1,11):
  print(i)

# while loop
i = 1
while i >=10:
  i = i+1
  print(i)


# Summary:
# 1. When the execution reaches the end of while statement's block, it jumps back to the start to re-check the condition.
#2. Press ctrl-c to interrupt infinite loop
#3. A break statement causes the execution to immediaetly exit the loop, withour re-checking.
#4. A continue statement causes the execution to immediaetly jump back to the start of the loop and re-check the condition.


