#Ex.156

# line = str(input('Enter a number: '))
# total = 0
#
# while line != "":
#     try:
#         total = total + float(line)
#         print(total)
#     except ValueError:
#         print("Value error! Try again...")
#
#     line = str(input('Enter a number: '))


#Ex.157

# grades = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0,
#           "C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0}
#
# val = str(input("Enter a letter grade or points: "))
#
# while val != '':
#     if val in grades.keys() or float(val) in grades.values():
#         try:
#             for i in grades:
#                 if grades[i] == float(val):
#                     print(i)
#         except ValueError:
#             if val in grades:
#                 print(grades[val])
#     else:
#         print("Invalid input")
#
#     val = str(input("Enter a letter grade or points: "))


#Ex.158

# fname = input("Enter an input file: ")
# fname2 = input("Enter an output file: ")
# try:
#     inf = open(fname, "r")
#     outf = open(fname2, "w")
#
#     line = inf.readline()
#     while line != "":
#         line = line.rstrip()
#         if line[0] != "#":
#             outf.write(line + "\n")
#         line = inf.readline()
#     inf.close()
#     outf.close()
# except FileNotFoundError:
#     print("File not found")


#Ex.159
# from random import randrange
#
# fname = "test1.txt"
# inf = open(fname, "r")
#
# words_l = []
# line = inf.readline()
# while line != '':
#     line = line.rstrip()
#     words_l.append(line)
#     line = inf.readline()
# inf.close()
#
# res = ""
# first_word = ""
# second_word = ""
#
# while first_word == "" and second_word == "":
#     first_word = words_l[randrange(0,len(words_l))]
#     second_word = words_l[randrange(0,len(words_l))]
#     if len(first_word) + len(second_word) <= 10:
#         if (len(first_word) and len(second_word)) > 3 and (len(first_word) and len(second_word)) < 8:
#             first_word = first_word.capitalize()
#             second_word = second_word.capitalize()
#             res += first_word
#             res += second_word
#         else:
#             first_word = ""
#             second_word = ""
#     else:
#         first_word = ""
#         second_word = ""
#
# print(res)


#Ex.160

# fname = "test160.txt"
# inf = open(fname, "r")
#
# except_words = []
# right_words = []
#
# line = inf.readline()
#
# while line != "":
#     line = line.rstrip()
#     if ("cei" in line  or "ie" in line) and line not in right_words:
#         right_words.append(line)
#     elif "ei" in line and line not in except_words:
#         except_words.append(line)
#     line = inf.readline()
#
# print(right_words)
# print(except_words)

