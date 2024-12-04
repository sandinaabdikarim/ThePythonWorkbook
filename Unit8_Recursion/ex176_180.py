#Ex.176

# def natoFonAlphabet(word, res):
#     alphabet = {"A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot",
#                 "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet", "K": "Kilo", "L": "Lima", "M": "Mike",
#                 "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Rome", "S": "Sierra", "T": "Tango",
#                 "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "Xray", "Y": "Yankee", "Z": "Zulu"}
#
#     if word == "":
#         return res
#
#     tail = word[1:len(word)]
#     if word[0] in alphabet:
#         res += alphabet[word[0]] + " "
#         return natoFonAlphabet(tail, res)
#
# def main():
#
#     line = str(input("Enter a word: "))
#     line = line.upper()
#     result = ""
#     print(natoFonAlphabet(line, result))
# main()


#Ex.177

# def romanNumber(n, res):
#     numbers = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
#
#     if n == "":
#         return res
#
#     tail = n[2:len(n)]
#
#     if len(n) >= 2:
#         if n[0] == "C" or n[0] == "X" or n[0] == "I":
#             if numbers[n[1]] == numbers[n[0]] * 10:
#                 res += (numbers[n[1]] - numbers[n[0]])
#             else:
#                 res += numbers[n[0]] + numbers[n[1]]
#         else:
#             res += numbers[n[0]] + numbers[n[1]]
#     else:
#         res += numbers[n[0]]
#
#     return romanNumber(tail, res)
#
# def main():
#     num = str(input("Enter a number in Roman: "))
#     num = num.upper()
#     result = 0
#     print(romanNumber(num, result))
# main()


#Ex.178
#
# def palindrome(word, rev_word):
#
#     tail = word[1:len(word)]
#     rev_tail = rev_word[1:len(rev_word)]
#     is_Palindrome = True
#
#     if word == "":
#         return is_Palindrome
#
#     if word[0] != rev_word[0]:
#         is_Palindrome = False
#         return is_Palindrome
#     else:
#         return palindrome(tail, rev_tail)
#
# def main():
#     line = str(input("Enter a word: "))
#     rev_line = line[::-1]
#     line = line.lower()
#     rev_line = rev_line.lower()
#
#     if palindrome(line, rev_line):
#         print("The word is a palindrome")
#     else:
#         print("The word is not a palindrome")
# main()


#Ex.179

# def squareRoot(n, guess=1.0):
#
#     if abs(guess ** 2 - n ) <= 10 ** (-12):
#         return guess
#     else:
#         return squareRoot(n, (guess + n / guess) / 2)
#
# def main():
#     num = int(input("Enter a number: "))
#     print(squareRoot(num))
# main()


#Ex.180

# def stringEditDistance(s, t):
#
#     if len(s) == 0:
#         return len(t)
#     elif len(t) == 0:
#         return len(s)
#     else:
#         cost = 0
#         if s[-1] != t[-1]:
#             cost += 1
#         d1 = stringEditDistance(s[:-1], t) + 1
#         d2 = stringEditDistance(s, t[:-1]) + 1
#         d3 = stringEditDistance(s[:-1], t[:-1]) + cost
#         return min(d1, d2, d3)
# def main():
#     str1 = str(input("Enter a word: "))
#     str2 = str(input("Enter a word: "))
#     print(stringEditDistance(str1, str2))
# main()

