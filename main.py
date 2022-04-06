# ask the user for a number and store in a variable num
num = input("Enter number")

#OPTIONAL validate that what they have entered is a number
while not num.isdecimal():
  #keep looping until they enter a number
  num = input("Not an integer  - Enter number")
#change the entered number into an integer - remember input() will always return a string
num = int(num)

# loop from 1 to 12 - remember range doesn't go up t o that last number in the brackets
for i in range(1,13):
  # print out the string 1 x 7 = 7
  # where 1 is i
  # where 7 is num
  # and the answer is i * num
  # all of the numbers have to be turned to strings using str()
  print(str(i) + " x " + str(num) + " = " + str(i*num))