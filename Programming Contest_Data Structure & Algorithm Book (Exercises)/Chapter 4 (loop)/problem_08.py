"""
Check whether a given number is a palindrome or not
"""

num = int(input("Enter an integer number: "))

temp = num
rev = 0

while (num > 0):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if (temp == rev):
    print("The given number is Palindrome...!")
else:
    print("The given number is not a Palindrome...!")