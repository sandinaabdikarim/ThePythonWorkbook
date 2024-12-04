#Ex.149

# fname = input('Enter a file name: ')
# try:
#     inf = open(fname, "r")
#     for line in range(10):
#         line = inf.readline()
#         print(line)
#     inf.close()
# except FileNotFoundError:
#     print('File not found')
#     quit()


#Ex.150

# fname = input('Enter a file name: ')
# l = []
# try:
#     inf = open(fname, "r")
#     last_items = inf.readlines()[-10:]
#     for i in last_items:
#         i = i.rstrip()
#         l.append(i)
#     inf.close()
# except FileNotFoundError:
#     print('File not found')
#     quit()
# print(l)


#Ex.151
# s = []
# line = input("Enter a file name: ")
# while line != "":
#     s.append(line)
#     line = input("Enter a file name: ")
#
# for file_name in s:
#     try:
#         fname = open(file_name, "r")
#         l_file = fname.readlines()
#         for i in l_file:
#             i = i.rstrip()
#             print(i)
#             fname.close()
#     except:
#         print("Could not open file with name", fname)


#Ex.152

# fname = input("Enter a file name to read: ")
# inf = open(fname, "r")
# fname2 = input("Enter a file name to write: ")
# outf = open(fname2, "w")
# line = inf.readline()
# num = 1
# res = ""
# while line != "":
#     line = line.rstrip()
#     res += str(num) + ": " + line
#     outf.write(res + "\n")
#     num += 1
#     res = ""
#     line = inf.readline()
# inf.close()
# outf.close()


#Ex.153

# fname = "test1.txt"
# inf = open(fname, "r")
#
# list = []
# line = inf.readline()
# while line!= '':
#     line = line.rstrip()
#     list.append(line)
#     line = inf.readline()
#
# inf.close()
#
# prev = list[0]
# res = []
# for i in list:
#     if len(i) > len(prev):
#         prev = i
#
# for i in list:
#     if len(i) == len(prev):
#         res.append(i)
# print(len(prev))
# print(res)


#Ex.154

# def decodeFile(s):
#
#     alphabet = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0,
#                 "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0,
#                 "W": 0, "X": 0, "Y": 0, "Z": 0}
#
#     for letter in s:
#         if letter in alphabet:
#             alphabet[letter] += 1
#
#     return alphabet
#
# def main():
#     fname = input("Enter a file name: ")
#     try:
#         inf = open(fname, "r")
#
#         sentence = ""
#         line = inf.readline()
#         while line != '':
#             line = line.rstrip()
#             line = line.upper()
#             sentence += line
#             line = inf.readline()
#         inf.close()
#         result = decodeFile(sentence)
#         print(result)
#     except:
#         print("Error! Could not open file!")
# main()


#Ex.155

# def onlyWords(s):
#
#     data = []
#     words = ''
#     marks = [",", ".", ":", "!", "?", ";", " "]
#     for i in range(len(s)):
#         if s[i] in marks:
#             if words != "":
#                 data.append(words)
#             words = ''
#         else:
#             words += s[i]
#
#         if i == len(s) -1 and words != "":
#             data.append(words)
#
#     return data
#
# def freqWords(l):
#
#     words_dict = {}
#     for i in range(len(l)):
#         if l[i] not in words_dict:
#             words_dict[l[i]] = 0
#
#     for word in l:
#         words_dict[word] += 1
#
#     return words_dict
#
# def main():
#     fname = input("Enter a file name: ")
#     try:
#         inf = open(fname, "r")
#
#         sentence = ""
#         line = inf.readline()
#         while line != '':
#             line = line.rstrip()
#             line = line.lower()
#             sentence += line + " "
#             line = inf.readline()
#         inf.close()
#         res_list = onlyWords(sentence)
#         result = freqWords(res_list)
#         print(result)
#     except:
#         print("Error! Could not open file!")
# main()

