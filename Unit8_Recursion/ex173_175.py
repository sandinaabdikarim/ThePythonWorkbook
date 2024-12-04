#Ex.173

# def sum_to():
#     num = str(input("Enter a number: "))
#     if num == "":
#         return 0
#     else:
#         return int(num) + sum_to()
# def main():
#     print(sum_to())
# main()


#Ex.174

# def NOD(a, b):
#     if b == 0:
#         return a
#     else:
#         c = a % b
#         return NOD(b, c)
#
# def main():
#     n1 = int(input("Enter the first number: "))
#     n2 = int(input("Enter the second number: "))
#     print(NOD(n1, n2))
# main()


#Ex.175


# def decToBin(num, result):
#     if num == 0:
#         result += "0"
#         return result
#     elif num == 1:
#         result += "1"
#         return result
#     else:
#         r = num % 2
#         result += str(r)
#         return decToBin(num // 2, result)
#
# def main():
#     n = int(input("Enter a number: "))
#     res = decToBin(n, "")
#     res = res[::-1]
#     print(res)
# main()

