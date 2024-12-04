#Ex.181

# def possibleChange(amount, num_coins):
#     print(amount)
#     is_possible = False
#     coin = 0
#     if amount == 0 and num_coins == 0:
#         return True
#     elif amount == 0 and num_coins > 0:
#         return False
#     elif amount > 0 and num_coins == 0:
#         return False
#
#     if amount >= 25:
#         is_possible = possibleChange(amount - 25, num_coins - 1)
#         coin = 25
#     if not is_possible and amount >=10:
#         is_possible = possibleChange(amount - 10, num_coins - 1)
#         coin = 10
#     if not is_possible and amount >=5:
#         is_possible = possibleChange(amount - 5, num_coins - 1)
#         coin = 5
#     if not is_possible and amount >=1:
#         is_possible = possibleChange(amount - 1, num_coins - 1)
#         coin = 1
#
#     return is_possible
#
# def main():
#     dollar = float(input("Enter a dollar amount: "))
#     number = int(input("Enter a number of coins: "))
#
#
#     if possibleChange(dollar * 100, number):
#         print("It is possible")
#     else:
#         print("It is NOT possible")
# main()

#Ex.182

# def loadElements():
#     fname = "elements.txt"
#     inf = open(fname, "r")
#     abbreviations = []
#     for line in inf:
#         line = line.rstrip()
#         l_line = line.split(",")
#         abbreviations.append(l_line[1])
#     inf.close()
#     return abbreviations
#
# def spellingSymbols(word, words):
#
#     if word == "":
#         return ""
#
#     s = ""
#     count = 1
#     while len(word) > 0:
#         letter = word[:count].capitalize()
#         if letter in words:
#             idx = words.index(letter)
#             s += words[idx]
#             s1 = spellingSymbols(word[count:], words)
#             return s + s1
#         if letter not in words:
#             count += 1
#         if count > len(word):
#             return s
#
# def main():
#     name = str(input("Enter a name of the element: "))
#     elements = loadElements()
#     result = spellingSymbols(name, elements)
#     if result.lower() != name.lower():
#         print("This element couldn't be spelled")
#     else:
#         print(f"{name} can be spelled as {result}")
#
# main()


#Ex.183

# def elementsSequences(word, elements, result=[]):
#     if word[-1].capitalize() not in elements:
#         return result
#
#     count = 0
#     while count < len(elements[word[-1].capitalize()]) and elements[word[-1].capitalize()][count] in result:
#         count += 1
#
#     if count == len(elements[word[-1].capitalize()]):
#         return result
#
#     result.append(elements[word[-1].capitalize()][count])
#     return elementsSequences(elements[word[-1].capitalize()][count], elements, result)
#
# def main():
#     l_elements = {"A":[], "B":[], "C":[], "D":[], "E":[], "F":[], "G":[], "H":[], "I":[], "J":[], "K":[], "L":[],
#                   "M":[], "N":[], "O":[], "P":[], "Q":[], "R":[], "S":[], "T":[], "U":[], "V":[], "W":[],
#                   "X":[], "Y":[], "Z":[]}
#     fname = "elements.txt"
#     inf = open(fname, "r")
#     line = inf.readline()
#     while line != '':
#         line = line.rstrip()
#         l_line = line.split(",")
#         if l_line[2][0] in l_elements:
#             l_elements[l_line[2][0]].append(l_line[2])
#         line = inf.readline()
#     inf.close()
#
#     user_word = input("Enter a name of the element: ")
#     print(elementsSequences(user_word, l_elements))
# main()


# def longestSequence(start, words):
#     if start == "":
#         return []
#
#     best = []
#     last_letter = start[len(start) - 1].lower()
#     for i in range(0, len(words)):
#         first_letter = words[i][0].lower()
#         if first_letter == last_letter:
#             candidate = longestSequence(words[i], words[0:i] + words[i + 1:len(words)])
#             if len(candidate) > len(best):
#                 best = candidate
#     return [start] + best
#
# def loadNames():
#     names = []
#     inf = open("elements.txt", "r")
#     for line in inf:
#         line = line.rstrip()
#         parts = line.split(",")
#         names.append(parts[2])
#     inf.close()
#     return names
#
# def main():
#     names = loadNames()
#     start = str(input("Enter start word: "))
#     start = start.capitalize()
#
#     if start in names:
#         names.remove(start)
#         sequence = longestSequence(start, names)
#         print(sequence)
#         for element in sequence:
#             print(element)
#     else:
#         print("Sorry, not valid")
# main()


#Ex.184

# def flatteningList(data):
#     if data == []:
#         return []
#
#     if type(data[0]) == list:
#         l1 = flatteningList(data[0])
#         l2 = flatteningList(data[1:])
#         return l1 + l2
#     if type(data[0]) != list:
#         l1 = data[0]
#         l2 = flatteningList(data[1:])
#         return [l1] + l2
#
# def main():
#
#     l = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
#     print(flatteningList(l))
# main()


#Ex.185

# def runLenghtsCoding(data):
#     if data == []:
#         return []
#
#     l = []
#     l.append(data[0])
#     for i in range(1, data[1]):
#         l.append(data[0])
#     l1 = runLenghtsCoding(data[2:])
#     return l + l1
#
# def main():
#     l_data = ['A', 12, 'B', 4, 'A', 6, 'B', 1]
#     print(runLenghtsCoding(l_data))
# main()


#Ex.186


# def runLengthDecoding(data):
#
#     if data == []:
#         return []
#     count = 0
#     l = []
#     l.append(data[0])
#     for i in range(len(data)):
#         if data[i] == data[0]:
#             count += 1
#         else:
#             l.append(count)
#             l1 = runLengthDecoding(data[i:])
#             return l + l1
#     l.append(count)
#     return l
# def main():
#
#     l_data = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
#     print(runLengthDecoding(l_data))
# main()

