#Ex.79

# m = int(input("Enter a number: "))
# n = int(input("Enter a second number: "))
#
# d = min(m, n)
#
# while m % d != 0  or n % d != 0:
#     d -= 1
#
# print(d)


#Ex.80

# n = int(input("Enter an integer 2 or greater: "))
#
# factor = 2
# print(f"The prime factors of {n}: ")
# while factor <= n:
#     if n % factor == 0:
#         print(factor)
#         n = n / factor
#     else:
#         factor += 1


#Ex.81

# n_base_two = str(input("Enter a number in base 2: "))
# n_base_two = n_base_two[::-1]
# n_base_ten = 0
# idx = 0
#
# for i in n_base_two:
#     n_base_ten += int(i) * 2 ** idx
#     idx += 1
#
# print(n_base_ten)


#Ex.82

# q = int(input("Enter a number in base 10: "))
# result = ''
#
# while q > 0:
#     r = q % 2
#     result += str(r)
#     q //= 2
# result = result[::-1]
# print(result)


#Ex.83


# from random import randrange
#
# num_items = 100
# max_value = randrange(1, num_items + 1)
# print(max_value)
# count = 0
#
# for i in range(1, num_items):
#     current_value = randrange(1, num_items + 1)
#     if current_value > max_value:
#         max_value = current_value
#         count += 1
#         print(current_value, "<=== Update")
#     else:
#         print(current_value)
#
# print("The maximum value was updated ", count)


#Ex.84
# import random
#
# ave_flips = 0
# for i in range(10):
#     flips = 0
#     res_string = ""
#     heads = 0
#     tails = 0
#     while heads != 3 and tails != 3:
#         coin = random.randint(0,1)
#         if coin == 0:
#             heads += 1
#             tails = 0
#             res_string += "H "
#         elif coin == 1:
#             tails += 1
#             heads = 0
#             res_string += "T "
#         flips += 1
#     print(res_string, end="  ")
#     print(f"({flips} flips)")
#     ave_flips += flips
# print(f"On average, {ave_flips / 10} flips were needed")