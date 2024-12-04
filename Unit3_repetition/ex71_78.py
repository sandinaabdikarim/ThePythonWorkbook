#Ex.71

# first_x = 2
# first_y = 3
# first_z = 4
#
# second_x = first_x
# second_y = first_y
# second_z = first_z
#
# count_approx = 1
#
# pi = "3 +"
# approx = f" (4 / {first_x} * {first_y} * {first_z})"
# pi += approx
# while count_approx < 15:
#     if count_approx % 2 == 0:
#         x = first_x + 2
#         y = first_y + 2
#         z = first_z + 2
#         approx = f" + (4 / {x} * {y} * {z})"
#         pi += approx
#         first_x = x
#         first_y = y
#         first_z = z
#         count_approx += 1
#
#     else:
#         x = first_x + 2
#         y = first_y + 2
#         z = first_z + 2
#         approx = f" - (4 / {x} * {y} * {z})"
#         pi += approx
#         first_x = x
#         first_y = y
#         first_z = z
#         count_approx += 1
# print(pi)


#Ex.72


# for i in range(1,101):
#     if i % 3 == 0:
#         print("fizz")
#         continue
#     elif i % 5 == 0:
#         print("buzz")
#         continue
#     else:
#         print(i)


#Ex.73

# r_alphabet = "abcdefghijklmnopqrstuvwxyz"
#
# line = str(input("Enter a word: ")).lower()
# shift_amount = int(input("Enter a shift amount: "))
# cipher_line = ""
#
# if line.isalpha():
#     for i in line:
#         idx = r_alphabet.index(i)
#         if r_alphabet.index(i) + shift_amount >= len(r_alphabet):
#             n_idx = -(len(r_alphabet) - idx - shift_amount)
#         else:
#             n_idx = idx + shift_amount
#
#         cipher_line += r_alphabet[n_idx]
#
#     print(cipher_line)
# else:
#     print("Your word has numbers")


#Ex.74

# x = int(input("Enter x: "))
#
# guess = x / 2
#
# while abs(guess * guess - x) >= 10 ** (-12):
#     guess = (guess + x / guess) / 2
#     print(guess)


#Ex.75

# line = str(input("Enter a word: "))
# rev_line = line[::-1]
# is_Palindrome = True
# for i in range(len(line)):
#     if line[i] != rev_line[i]:
#         is_Palindrome = False
#         break
# if is_Palindrome:
#     print("The word is palindrome.")
# else:
#     print("The word is not palindrome.")


#Ex.76

# line = str(input("Enter a sentence: "))
# line = line.replace(" ", "")
# line = line.lower()
# n_line = line[::-1]
#
# is_Palindrome = True
# for i in range(len(line)):
#     if line[i] != n_line[i]:
#         is_Palindrome = False
#         break
# if is_Palindrome:
#     print("The sentence is palindrome")
# else:
#     print("The sentence is not palindrome")


#Ex.77


# top_numbers = ""
# row_numbers = ""
# for i in range(1, 11):
#     top_numbers += str(i) + "  "
#     print("")
#     print(i, end="    ")
#     for j in range(1, 11):
#         row_numbers += str(j) + "  "
#         print(i * j, end="    ")


#Ex.78

# n = int(input("Enter a positive number: "))
#
# while n != 1:
#     if n % 2 == 0:
#         n = n / 2
#         print(n)
#     else:
#         n = 3 * n + 1
#         print(n)

