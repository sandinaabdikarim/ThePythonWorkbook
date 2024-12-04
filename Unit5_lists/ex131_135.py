#Ex.131

# def in_postfix(data):
#     operators = []
#     postfix = []
#     operator = ["+", "-", "*", "/", "(", ")", "u+", "u-"]
#
#     for i in data:
#         if i.isdigit():
#             postfix.append(i)
#         if i in operator:
#             while operators != [] and operators[-1] != "(" and precedence(i) < precedence(operators[-1]):
#                 tmp = operators.pop()
#                 postfix.append(tmp)
#
#             operators.append(i)
#         if i == "(":
#             operators.append(i)
#         if i == ")":
#             while operators[-1] != "(":
#                 tmp = operators.pop()
#                 postfix.append(tmp)
#             operators.remove("(")
#
#     while operators != []:
#         tmp = operators.pop()
#         postfix.append(tmp)
#
#     return postfix
#
# def precedence(s):
#     prioritize = 0
#     if s.count('^') > 0:
#         prioritize = 3
#     elif s.count('*') > 0 or s.count('/') > 0:
#         prioritize = 2
#     elif s.count('+') > 0 or s.count('-') > 0:
#         prioritize = 1
#     else:
#         prioritize = -1
#
#     return prioritize
#
# def tokenizingString(s):
#     s = s.replace(' ', '')
#
#     token = []
#     i = 0
#     operators = '*/+-()'
#     numbers = '0123456789'
#     while i < len(s):
#         if s[i] in operators:
#             token.append(s[i])
#             i += 1
#         elif s[i] in numbers:
#             num = ''
#             while i < len(s) and s[i] in numbers:
#                 num += s[i]
#                 i += 1
#             token.append(num)
#         else:
#             return []
#     return token
#
# def unaryOperators(tokens):
#     operators = '*/+-()'
#     data = tokens.copy()
#
#     for i in range(len(data)):
#         if i == 0:
#             if data[i] == "+":
#                 data[i] = "u+"
#             elif data[i] == "-":
#                 data[i] = "u-"
#         else:
#             if data[i] == "+" and data[i-1] in operators:
#                 data[i] = "u+"
#             elif data[i] == "-" and data[i-1] in operators:
#                 data[i] = "u-"
#     return data
#
#
# def main():
#     exp = input('Enter an expression: ')
#     tokens = tokenizingString(exp)
#     u_tokens = unaryOperators(tokens)
#     postfix_data = in_postfix(u_tokens)
#
#     print(tokens)
#     print(postfix_data)
#
# main()


#Ex.132
#
# def in_postfix(data):
#     operators = []
#     postfix = []
#     operator = ["+", "-", "*", "/", "(", ")", "u+", "u-"]
#
#     for i in data:
#         if i.isdigit():
#             postfix.append(i)
#         if i in operator:
#             while operators != [] and operators[-1] != "(" and precedence(i) < precedence(operators[-1]):
#                 tmp = operators.pop()
#                 postfix.append(tmp)
#
#             operators.append(i)
#         if i == "(":
#             operators.append(i)
#         if i == ")":
#             while operators[-1] != "(":
#                 tmp = operators.pop()
#                 postfix.append(tmp)
#             operators.remove("(")
#
#     while operators != []:
#         tmp = operators.pop()
#         postfix.append(tmp)
#
#     return postfix
#
#
# def precedence(s):
#     prioritize = 0
#     if s.count('^') > 0:
#         prioritize = 3
#     elif s.count('*') > 0 or s.count('/') > 0:
#         prioritize = 2
#     elif s.count('+') > 0 or s.count('-') > 0:
#         prioritize = 1
#     else:
#         prioritize = -1
#
#     return prioritize
#
# def tokenizingString(s):
#     s = s.replace(' ', '')
#
#     token = []
#     i = 0
#     operators = '*/+-()'
#     numbers = '0123456789'
#     while i < len(s):
#         if s[i] in operators:
#             token.append(s[i])
#             i += 1
#         elif s[i] in numbers:
#             num = ''
#             while i < len(s) and s[i] in numbers:
#                 num += s[i]
#                 i += 1
#             token.append(num)
#         else:
#             return []
#     return token
#
# def unaryOperators(tokens):
#     operators = '*/+-()'
#     data = tokens.copy()
#
#     for i in range(len(data)):
#         if i == 0:
#             if data[i] == "+":
#                 data[i] = "u+"
#             elif data[i] == "-":
#                 data[i] = "u-"
#         else:
#             if data[i] == "+" and data[i-1] in operators:
#                 data[i] = "u+"
#             elif data[i] == "-" and data[i-1] in operators:
#                 data[i] = "u-"
#     return data
#
# def postfix(data):
#     values = []
#
#     for i in data:
#         if i.isdigit():
#             values.append(i)
#         elif i == '-' or i == '+' or i == '*' or i == '/':
#             right = values.pop()
#             left = values.pop()
#             result = left + i + right
#             values.append(result)
#         if i == "u-":
#             values.insert(0, "-")
#         if i == "u+":
#             values.insert(0, "+")
#     res = ""
#     for i in range(len(values)):
#         res += str(values[i])
#     return res
#
# def main():
#     exp = input('Enter an expression: ')
#     tokens = tokenizingString(exp)
#     u_tokens = unaryOperators(tokens)
#     infix_data = in_postfix(u_tokens)
#     postfix_data = postfix(infix_data)
#
#     print(tokens)
#     print(infix_data)
#     print(postfix_data)
#
# main()


# Ex.133
#
# def isSublist(larger, smaller):
#     point_s = 0
#     is_Sublist = False
#     i = 0
#
#     while i < len(larger):
#         if i <= len(smaller):
#             if larger[i] == smaller[point_s]:
#                 i += 1
#                 point_s += 1
#                 if point_s == len(smaller):
#                     is_Sublist = True
#                     break
#             elif larger[i] != smaller[point_s]:
#                 i += 1
#                 point_s = 0
#         else:
#             is_Sublist = False
#             return is_Sublist
#
#
# def main():
#     num_l = (input("Enter a big list: "))
#     big_l = []
#     while num_l != "":
#         big_l.append(num_l)
#         num_l = (input("Enter a big list: "))
#
#     num_s = (input("Enter a small list: "))
#     small_l = []
#
#     while num_s != "":
#         small_l.append(num_s)
#         num_s = (input("Enter a small list: "))
#
#     result = isSublist(big_l, small_l)
#     print(result)
# main()


#Ex.134

# def allSublists(data):
#
#     sublists = [[]]
#
#     for lenght in range(1, len(data) + 1):
#         for i in range(0, len(data) - lenght + 1):
#             sublists.append(data[i:i + lenght])
#
#     return sublists
#
# def main():
#     print(allSublists([1, 2, 3]))
#     print(allSublists([1, 2, 3, 4, 5]))
# main()


#Ex.135

# n = int(input("Enter a number: "))
# data = [0] * (n + 1)
#
# data[0] = 0
# data[1] = 1
# data[2] = 2
#
# for i in range(3, n+1):
#     is_prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         data[i] = i
# print(data)

# data = [i for i in range(0, n + 1)]
# data[1] = 0
# p = 2
#
# while p <= n:
#     for i in range(0, n + 1):
#         if data[i] % p == 0:
#             if data[i] != p:
#                 data[i] = 0
#     p += 1
#
# print(data)

