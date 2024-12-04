#Ex.141

# def writtingEnglish(number):
#     result = ''
#     name_hundred = ''
#     name_dozens = ''
#     name_units = ''
#
#     units = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
#              8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
#              15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
#     dozens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
#               80: 'eighty', 90: 'ninety'}
#
#     hundreds = 0
#     dozens_n = 0
#     units_n = 0
#     while units_n != number:
#         if number >= 100:
#             hundreds = number // 100
#             number = number % 100
#         elif number >= 20:
#             dozens_n = (number // 10) * 10
#             number = number % 10
#         elif number >= 10 and number <= 19:
#                 units_n = number
#                 break
#         else:
#             units_n = number
#             break
#
#     for key in units:
#         if key == hundreds:
#             name_hundred += units[key] + ' hundred'
#         if key == units_n:
#             name_units += units[key]
#
#     for key in dozens:
#         if key == dozens_n:
#                 name_dozens += dozens[key]
#
#     result = name_hundred + ' ' + name_dozens + ' ' + name_units
#     return result
#
# def main():
#     n = int(input("Enter a number: "))
#     res = writtingEnglish(n)
#     print(res)
# main()


#Ex.142

# s = str(input("Enter a string: "))
#
# uni_characters = {}
#
# for i in s:
#     uni_characters[i] = True
#
# print(len(s))
# print(len(uni_characters))
# print(uni_characters)


#Ex.143

# word1 = str(input("Enter the first word: "))
# word2 = str(input("Enter the second word: "))
#
# word1 = word1.lower()
# word2 = word2.lower()
#
# l_word1 = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
#            "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
#            "y": 0, "z": 0}
# l_word2 = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
#            "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
#            "y": 0, "z": 0}
#
# is_anagram = True
#
# for i in range(len(word1)):
#     l_word1[word1[i]] += 1
#
# for k in range(len(word2)):
#     l_word2[word2[k]] += 1
#
# for j in l_word1:
#     if l_word1[j] != l_word2[j]:
#         is_anagram = False
#         break
#
# print(is_anagram)


#Ex.144

# word1 = str(input("Enter the first word: "))
# word2 = str(input("Enter the second word: "))
#
# word1 = word1.lower()
# word2 = word2.lower()
#
# l_word1 = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
#            "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
#            "y": 0, "z": 0}
# l_word2 = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
#            "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
#            "y": 0, "z": 0}
#
# marks = " .,?!"
# is_anagram = True
#
# for i in range(len(word1)):
#     if word1[i] in marks:
#         continue
#     else:
#         l_word1[word1[i]] += 1
#
# for k in range(len(word2)):
#     if word2[k] in marks:
#         continue
#     else:
#         l_word2[word2[k]] += 1
#
# for j in l_word1:
#     if l_word1[j] != l_word2[j]:
#         is_anagram = False
#         break
#
# print(is_anagram)


#Ex.145

# def scrabbleScore(word):
#
#     word = word.upper()
#     letter_points = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "R": 1, "S": 1, "T": 1, "N": 1, "D": 2,
#                      "G": 2, "B": 3, "C": 3, "M": 3, "P": 3, "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4, "K": 5,
#                      "J": 8, "X": 8, "Q": 10, "Z": 10}
#     count = 0
#     for i in word:
#         if i in letter_points:
#             count += letter_points[i]
#
#     return count
#
# def main():
#     s = str(input("Enter a word: "))
#     res = scrabbleScore(s)
#     print(res)
# main()
