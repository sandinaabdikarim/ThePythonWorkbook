#Ex.136

# def reverseLookup(dict, value):
#     count_d = []
#
#     for i in dict:
#         if dict[i] == value:
#             count_d.append(i)
#
#     return count_d
#
# def main():
#
#     d = {"person1": "John", "person2": "Smith", "person3" : "John", "person4" : "Kim", "person5" : "Kate"}
#     res = reverseLookup(d, "John")
#     print(res)
# main()


#Ex.137

# from random import randrange
#
# def twoDiceSimulation():
#     dice1 = randrange(1, 7)
#     dice2 = randrange(1, 7)
#
#     return dice1 + dice2
#
# def main():
#     expected = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
#                 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}
#
#     counts = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
#
#     for i in range(1000):
#         t = twoDiceSimulation()
#         counts[t] += 1
#     print("       Percent    Percent")
#     for i in sorted(counts.keys()):
#         print("%5d %11.2f.  %8.2f" % (i, counts[i]/1000 * 100, expected[i] * 100))
#
# main()


#Ex.138

# symbols = {1: ".,?!:", 2: "ABC", 3: "DEF", 4: "GHI", 5: "JKL", 6: "MNO", 7: "PQRS", 8: "TUV", 9: "WXYZ", 0: " "}
#
# s = str(input("Enter a string: "))
# s = s.upper()
# res = ""
#
# for i in range(len(s)):
#     for j in symbols.keys():
#         if s[i] in symbols[j]:
#             for m in symbols[j]:
#                 if s[i] == m:
#                     res += str(j)
#                     break
#                 res += str(j)
#
# print(res)


#Ex.139

# morse_code = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
#               "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--",
#               "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
#               "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----",
#               "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
#               "7": "--...", "8": "---..", "9": "----."}
#
# s = str(input("Enter a sentence: "))
# s = s.upper()
#
# res = ""
# for i in range(len(s)):
#     if s[i] in morse_code:
#         res += " " + morse_code[s[i]]
#
# print(res)


#Ex.140

# postal_code = {"Newfoundland": "A", "Nova Scotia": "B", "Prince Edward Island": "C", "New Brunswick": "E",
#                "Quebec": "GHJ", "Ontario": "KLMNP", "Manitoba": "R", "Saskatchewan": "S", "Alberta": "T",
#                "British Columbia": "V", "Nunavut": "X", "Northwest Territory": "X", "Yukon": "Y"}
#
# s = str(input("Enter a postal code: "))
# res = ""
# is_right = True
#
# if s[0].isalpha() and s[0] in postal_code.values():
#     for i in postal_code:
#         if s[0] in postal_code[i]:
#             res += i
# else:
#     is_right = False
#
# if s[1].isdigit():
#     if s[1] == "0":
#         res += " " + "rural"
#     else:
#         res += " " + "urban"
# else:
#     is_right = False
#
# if is_right:
#     print(res)
# else:
#     print("Wrong postal code")
