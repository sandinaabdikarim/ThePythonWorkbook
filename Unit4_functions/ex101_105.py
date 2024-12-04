#Ex.101

# from random import randint
#
# def oldNewPlate():
#     older_length = 6
#     new_length = 7
#
#     odd_even = randint(1, 10)
#     is_odd = False
#     if odd_even % 2 == 0:
#         is_odd = True
#     else:
#         is_odd = False
#
#     if is_odd:
#         return older_length
#     else:
#         return new_length
#
# def randomPlate():
#
#     length = oldNewPlate()
#     result = ''
#
#     for i in range(length):
#         if length == 6:
#             if 0 <= i <= 2:
#                 letter = chr(randint(65, 90))
#                 result += letter
#             else:
#                 number = randint(1, 9)
#                 result += str(number)
#         else:
#             if 0 <= i <= 3:
#                 number = randint(1, 9)
#                 result += str(number)
#             else:
#                 letter = chr(randint(65, 90))
#                 result += letter
#     return result
#
# def main():
#     res = randomPlate()
#     print(res)
#
# main()


#Ex.102

# def checkPassword(line):
#
#     uppercase_l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     lowercase_l = "abcdefghijklmnopqrstuvwxyz"
#     numbers = "0123456789"
#     has_upper = False
#     has_lower = False
#     has_number = False
#
#     if len(line) < 8:
#         return False
#     else:
#         for i in line:
#             if i in uppercase_l:
#                 has_upper = True
#             elif i in lowercase_l:
#                 has_lower = True
#             elif i in numbers:
#                 has_number = True
#
#         if has_upper and has_lower and has_number:
#             return True
#         else:
#             return False
#
# def main():
#     password = str(input("Enter a password: "))
#     print(checkPassword(password))
#
# main()


#Ex.103

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
# def checkPassword(line):
#
#     uppercase_l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     lowercase_l = "abcdefghijklmnopqrstuvwxyz"
#     numbers = "0123456789"
#     has_upper = False
#     has_lower = False
#     has_number = False
#
#     res = False
#
#     if len(line) < 8:
#         return res
#     else:
#         for i in line:
#             if i in uppercase_l:
#                 has_upper = True
#             elif i in lowercase_l:
#                 has_lower = True
#             elif i in numbers:
#                 has_number = True
#
#         if has_upper and has_lower and has_number:
#             res = True
#             return res
#         else:
#             return res
#
# def main():
#     password = randomPassword()
#     ch_password = checkPassword(password)
#     count = 0
#
#     while not ch_password:
#         count += 1
#         password = randomPassword()
#         ch_password = checkPassword(password)
#
#     print(password)
#     print(count)
#
# main()


#Ex.104

# def hex2int(s):
#     res = 0
#     numbers = "0123456789"
#     for i in s:
#         if i in numbers:
#             res += int(i) * 16 ** (len(s) - s.index(i) - 1)
#         if i == "A":
#             res += 10 * 16 ** (len(s) - s.index(i) - 1)
#         elif i == "B":
#             res += 11 * 16 ** (len(s) - s.index(i) - 1)
#         elif i == "C":
#             res += 12 * 16 ** (len(s) - s.index(i) - 1)
#         elif i == "D":
#             res += 13 * 16 ** (len(s) - s.index(i) - 1)
#         elif i == "E":
#             res += 14 * 16 ** (len(s) - s.index(i) - 1)
#         elif i == "F":
#             res += 15 * 16 ** (len(s) - s.index(i) - 1)
#     return res
#
# def int2hex(s):
#     res = ''
#
#     while s != 0:
#         remainder = s % 16
#         if 1 <= remainder <= 9:
#             res += str(remainder)
#         if remainder == 10:
#             res += "A"
#         elif remainder == 11:
#             res += "B"
#         elif remainder == 12:
#             res += "C"
#         elif remainder == 13:
#             res += "D"
#         elif remainder == 14:
#             res += "E"
#         elif remainder == 15:
#             res += "F"
#         s = int(s / 16)
#
#     res = res[::-1]
#     return res
#
# def main():
#     line = str(input("Enter a number in hexadecimal: "))
#     hex_num = hex2int(line)
#     dec_num = int2hex(hex_num)
#     print(hex_num, dec_num)
#
# main()

#Ex.105

# def arbitraryConvert2int(s, base):
#     res = 0
#     numbers = "0123456789"
#
#     for i in s:
#         if i in numbers:
#             res += int(i) * base ** (len(s) - s.index(i) - 1)
#         if i == "A":
#             res += 10 * base ** (len(s) - s.index(i) - 1)
#         elif i == "B":
#             res += 11 * base ** (len(s) - s.index(i) - 1)
#         elif i == "C":
#             res += 12 * base ** (len(s) - s.index(i) - 1)
#         elif i == "D":
#             res += 13 * base ** (len(s) - s.index(i) - 1)
#         elif i == "E":
#             res += 14 * base ** (len(s) - s.index(i) - 1)
#         elif i == "F":
#             res += 15 * base ** (len(s) - s.index(i) - 1)
#     return res
#
# def int2arbitrary(s, base):
#     res = ''
#
#     while s != 0:
#         remainder = s % base
#         if 0 <= remainder <= 9:
#             res += str(remainder)
#         if remainder == 10:
#             res += "A"
#         elif remainder == 11:
#             res += "B"
#         elif remainder == 12:
#             res += "C"
#         elif remainder == 13:
#             res += "D"
#         elif remainder == 14:
#             res += "E"
#         elif remainder == 15:
#             res += "F"
#         s = int(s / base)
#
#     res = res[::-1]
#     return res
#
# def main():
#     c_base = int(input("Enter the base of the current number: "))
#     curr_num = str(input(f"Enter a number in {c_base} base: "))
#     w_base = int(input("Enter a base you want to convert (2 to 16): "))
#
#     if w_base < 2 or w_base > 16 or c_base < 2 or c_base > 16:
#         print("The base out of range")
#         quit()
#     elif c_base != 10:
#         res_int = arbitraryConvert2int(curr_num, c_base)
#         int_res = int2arbitrary(res_int, w_base)
#         print(int_res)
#     else:
#         result = arbitraryConvert2int(curr_num, w_base)
#         print(result)
# main()