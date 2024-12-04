#Ex.96

# def isInteger(s):
#     s = s.strip(' ')
#
#     if s[0] == '+' or s[0] == '-' and s[1:].isdigit():
#         return True
#     elif s.isdigit():
#         return True
#     else:
#         return False
#
# def main():
#     string = input('Enter a string: ')
#     print(isInteger(string))
#
# main()


#Ex.97

# def precedence(s):
#     if s.count('^') > 0:
#         return 3
#     elif s.count('*') > 0 or s.count('/') > 0:
#         return 2
#     elif s.count('+') > 0 or s.count('-') > 0:
#         return 1
#     else:
#         return -1
#
# def main():
#     string = input("Enter a string: ")
#     result = precedence(string)
#     print(result)
#
# main()


#Ex.98


# def isNumberPrime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#
#     return True
#
# def main():
#     number = int(input('Enter a number: '))
#     print(isNumberPrime(number))
#
# main()


#Ex.99

# def isNumberPrime(num):
#
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#
#     return True
#
# def nextPrime(n):
#
#     if isNumberPrime(n):
#         return f"{n} is a prime number"
#     else:
#         is_number_prime = isNumberPrime(n)
#         while not is_number_prime:
#             is_number_prime = isNumberPrime(n)
#             if is_number_prime == False:
#                 n = n + 1
#             else:
#                 return f"{n} is the next prime number"
#
# def main():
#     number = int(input('Enter a number: '))
#     print(nextPrime(number))
#
# main()


#Ex.100
# from random import randint
#
# def randomPassword():
#     length = randint(7, 10)
#     password = ""
#     for i in range(length):
#         letter = randint(33, 126)
#         password += chr(letter)
#     return password
#
# def main():
#     ranpass = randomPassword()
#     print(ranpass)
#
# main()