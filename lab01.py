# Lab01 - Exercise01 - 521H0272
# (a): 15 ∗ 2 + 7 ∗ 8
print("a: " + str(15*2+7*8))
# (b): 20-15+15*2
print("b: " + str(20-15+15*2))
# (c): 20 + 30 − 3 ∗ 15 + 5 ∗ 5
print("c: " + str(20+30-3*15+5**2))
# (d):
print("d: ", ((4/6 + 2/6))/(5/2 + 1/2))
# (e): 
print("e: ", (14/2 + 7))
# (f):
print("f: ", (5*2)/(5-20*(3**2)+30))

# Lab01 - Exercise02
print("15*2+7*8=" + str(15*2+7*8))
print("20-15+15*2=" + str(20-15+15*2))
print("20+30-3*15+5**2=" + str(20+30-3*15+5**2))
print("(4/6 + 2/6))/(5/2 + 1/2)=", ((4/6 + 2/6))/(5/2 + 1/2))
print("(14/2 + 7)=", (14/2 + 7))
print("(5*2)/(5-20*(3**2)+30)=", (5*2)/(5-20*(3**2)+30))

# Lab01 - Exercise03 - 521H0272
n = int(input("Enter n: "))
def sumN(n):
  sum = 0
  if (n > 0):
    for i in range (n+1):
      sum = sum + i
    return sum
  elif (n < 0):
    for i in range(n, 0):
      sum = sum + i
    return sum
  else:
      return 0
print(sumN(n))

# Lab01 - Exercise04 - 521H0272
from re import A
# Lab01 - Exercise04 - 521H0272
# (a): remove all space (" ") then string the result string
A = input("Input your string: ")
B = A.split()
C = "".join(B)
print("a :" + C)
# (b): remove all space ("_") then string the result string
C = "_".join(B)
print("b :" + C)

# Lab01 - Exercise05 - 521H0272
user_input = input("Enter your (addition/subtraction/multiplication/division): ")
split_user_input = user_input.split()
x = int(split_user_input[0])
y = int(split_user_input[2])
operator = split_user_input[1]
def calc(x, y):
  if(operator == "+"):
    return x+y
  elif(operator == "-"):
    return x-y
  elif(operator == "*"):
    return x*y
  else:
    return x/y
print(calc(x, y))

# Lab01 - Exercise06 - 521H0272
Dict = {1: '+', 2: '-', 3: '*', 4: '/'}
user_input = input("Enter your (addition/subtraction/multiplication/division): ")
split_user_input = user_input.split()
x = int(split_user_input[0])
y = int(split_user_input[2])
operator = split_user_input[1]
