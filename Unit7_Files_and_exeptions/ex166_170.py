#Ex.166

# def addNames(fname, names):
#
#     inf = open(fname, 'r')
#     line = inf.readline()
#     while line != "":
#         line = line.rstrip()
#         l = line.split()
#         if l[0] not in names:
#             names[l[0]] = l[1]
#         line = inf.readline()
#     inf.close()
#     return names

# def main():
#
#     boys_name = {}
#     girls_name = {}
#
#     for year in range(1900, 2013):
#         g_fname = "../Unit7_Files_and_exeptions/BabyNames/" + str(year) + "_GirlsNames.txt"
#         b_fname = "../Unit7_Files_and_exeptions/BabyNames/" + str(year) + "_BoysNames.txt"
#
#         addNames(g_fname, girls_name)
#         addNames(b_fname, boys_name)
#
#     print("Girl's names that reached #1:")
#     for name in girls_name:
#         print(" ", name)
#     print()
#     print("Boys's names that reached #1:")
#     for name in boys_name:
#         print(" ", name)
# main()


#Ex.167

# def onlyWords(fname):
#
#     data = {}
#     words = ''
#     marks = [",", ".", ":", "!", "?", ";", " "]
#
#     inf = open(fname, "r")
#     line = inf.readline()
#     while line != "":
#         line = line.rstrip()
#         line = line.lower()
#         for i in range(len(line)):
#             if line[i] in marks:
#                 if words != "":
#                     data[words] = 0
#                 words = ''
#             else:
#                 words += line[i]
#
#             if i == len(line) - 1 and words != "":
#                 data[words] = 0
#         line = inf.readline()
#
#     return data
#
# def readDictionary():
#
#     inf = open("dictionary.txt", "r")
#     res = {}
#
#     line = inf.readline()
#     while line != "":
#         line = line.rstrip()
#         line = line.lower()
#         res[line] = 0
#         line = inf.readline()
#     inf.close()
#     return res
#
# def main():
#     fname = "test167.txt"
#
#     try:
#         inf = open(fname, "r")
#     except FileNotFoundError:
#         print("File not found")
#         quit()
#
#     dict_words = readDictionary()
#     f_words = onlyWords(fname)
#     misspelled = []
#
#     for i in f_words:
#         if i not in dict_words and i not in misspelled:
#             misspelled.append(i)
#
#     if len(misspelled) == 0:
#         print("There are no misspelled words")
#     else:
#         print(misspelled)
#
# main()


#Ex.168

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
# def main():
#     fname = str(input("Enter a file name: "))
#
#     try:
#         inf = open(fname, "r")
#     except FileNotFoundError:
#         print("File not found")
#         quit()
#
#     line = inf.readline()
#     count = 1
#     list_line = []
#     double = ''
#     str_double = ''
#     prev = ''
#     while line != "":
#         line = line.rstrip()
#         list_line += onlyWords(line)
#         for i in list_line:
#             if i == prev:
#                 double = i
#                 str_double = str(count)
#             prev = i
#         line = inf.readline()
#         count += 1
#
#     inf.close()
#
#     print(double)
#     print(str_double)
# main()

#Ex.169

# def redactingText(s):
#     sensative_info = ["wizard", "magic", "death"]
#     red_string = s.split()
#
#     for i in sensative_info:
#         for j in range(len(red_string)):
#             if i in red_string[j].lower():
#                 red_string[j] = red_string[j].lower().replace(i, "***")
#     res = ''
#     for j in red_string:
#         res += " " + str(j)
#
#     return res
#
# def main():
#     fname = str(input("Enter file name to read: "))
#     inf = open(fname, "r")
#     fname2 = str(input("Enter file name to write: "))
#     outf = open(fname2, "w")
#
#     res = ''
#     line = inf.readline()
#     while line != "":
#         line = line.rstrip()
#         res = redactingText(line)
#         outf.write(res + "\n")
#         line = inf.readline()
#
#     inf.close()
#     outf.close()
# main()


#Ex.170

# def onlyWords(s):
#
#     data = []
#     words = ''
#     marks = [",", ".", ":", "!", "?", ";", " ", "(", ")"]
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
#
# def main():
#     fname = str(input("Enter a file name: "))
#     try:
#          inf = open(fname, "r")
#     except FileNotFoundError:
#          print("File not found")
#          quit()
#
#     line = inf.readline()
#     line_num = 1
#     name_func = []
#     prev_line = ""
#     while line != "":
#         line = line.rstrip()
#         if ("def " in line) and ("#"  not in prev_line):
#             res = onlyWords(line)
#             name_func.append(res[1])
#             name_func.append(line_num)
#         prev_line = line
#         line = inf.readline()
#         line_num += 1
#     inf.close()
#     print(name_func)
# main()
