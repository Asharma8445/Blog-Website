# If a number is even, and ranges between 60 and 80, then it's valid number or else not.
n = 66
# if n > 60 and n < 80:
#     print("It's a valid number")
# else: 
#     print("Invalid number")

# I need to hire only adult males. 

# 90 - 100% -> You got A grade | 80-90 -> B grade | 70-80 -> C grade | 60-70 -> D grade | 50-60 -> E | < 50 -> Failed

# num = int(input("Enter your marks percentage"))
# if num >= 90:
#     print("You got A grade")

# elif num >= 80:
#     print("You got B grade")

# elif num >= 70:
#     print("You got C grade")
# # 78
# elif num >= 60:
#     print("You got D grade")

# elif num >= 50:
#     print("You got E grade")

# else: 
#     print("You failed")


# Take 3 numbers, print which one is the biggest and smallest of these 3. 

# 45 78 99

# Conditional control structure: if | else | elif

# a = int(input("Enter a number: "))
# b = int(input("Enter 2nd number: "))
# c = int(input("Enter 3rd number: "))

# if a != b and b != c:
#     if a > b and a > c:
#         print("Biggest:", a)
#         if b > c:
#             print("Middle:", b)
#             print("Smallest:", c)
#         else: 
#             print("Middle:", c)
#             print("Smallest:", b)

#     elif b > a and b > c:
#         print("Biggest:", b)
#         if a > c:
#             print("Middle:", a)
#             print("Smallest:", c)
#         else: 
#             print("Middle:", c)
#             print("Smallest:", b)

#     elif c > a and c > b:
#         print("Biggest:", c)
#         if a > b:
#             print("Middle:", a)
#             print("Smallest:", b)
#         else: 
#             print("Middle:", b)
#             print("Smallest:", a)

#     else: 
#         print("Something went wrong. All the 3 numbers are equal")
# else: 
#         print("Something went wrong. 2 numbers are equal")

# 3. Iterative control structure: Loops. 
# While(Definite number) | For(Iteration over any collection of data)

# names = ["Pranjul", "Abhishek", "Raghav", "Hrithik", "Manjeet", "Haaris"]
# for i in names:
#     # print(i)
#     if len(i) > 6:
#         print(i)

#         startswith() 


# While loop: 
# Initialization

# while condition:
#     statements
#     update statement

# n = 89
# while n >= 1:
#     if (n % 2 == 0):
#         print(n)
#     n = n - 1

# Armstrong Number

n = int(input("Enter any number: "))
sum = 0
temp = n 
while temp > 0:
    digit = temp % 10
    sum += (digit ** 3)
    temp //= 10
    print (sum, digit, temp)

if sum == n:
    print("It is an armstrong number")
else:
    print("Not an armstrong number")