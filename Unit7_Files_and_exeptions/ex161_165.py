#Ex.161

# fname = "elements.txt"
# inf = open(fname, "r")
#
# elements = {}
#
# line = inf.readline()
# while line != "":
#     line = line.rstrip()
#     l = line.split(",")
#     elements[l[0]] = l[1] + "," + l[2]
#     line = inf.readline()
#
# value = str(input("Enter a proton of elements: "))
#
# while value != "":
#     if value.isdigit():
#         print(value, elements[value])
#     elif value.isalpha():
#         for i in elements:
#             if value in elements[i]:
#                 print(i, elements[i])
#                 break
#     value = str(input("Enter a proton of elements: "))


#Ex.162

# alphabet = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0,
#                 "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0,
#                 "W": 0, "X": 0, "Y": 0, "Z": 0}
#
# fname = "test1.txt"
# inf = open(fname, "r")
#
# line = inf.readline()
# count_letters = 0
# while line != "":
#     line = line.rstrip()
#     line = line.upper()
#     for letter in line:
#         if letter in alphabet:
#             alphabet[letter] += 1
#             count_letters += 1
#     line = inf.readline()
# percent_alphabet = {}
#
# for i in alphabet:
#     percent_alphabet[i] = (alphabet[i] * 100) / count_letters
#
# total = 0
# for j in percent_alphabet:
#     total += percent_alphabet[j]
# print(percent_alphabet)
# print(total)


#Ex.163

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
#
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


#Ex.164

# def addNames(fname, names):
#
#     inf = open(fname, 'r')
#     line = inf.readline()
#     while line != "":
#         line = line.rstrip()
#         l = line.split()
#         if l[0] not in names:
#             names.append(l[0])
#         line = inf.readline()
#     inf.close()
#     return names
#
# def main():
#
#     year = int(input('Enter year: '))
#
#     boys_name = []
#     girls_name = []
#     uniq_names = []
#
#     g_fname = "../Unit7_Files_and_exeptions/BabyNames/" + str(year) + "_GirlsNames.txt"
#     b_fname = "../Unit7_Files_and_exeptions/BabyNames/" + str(year) + "_BoysNames.txt"
#
#     addNames(g_fname, girls_name)
#     addNames(b_fname, boys_name)
#
#     for i in girls_name:
#         for j in boys_name:
#             if i == j and i not in uniq_names:
#                 uniq_names.append(i)
#
#     print("Unique names: ")
#     print(uniq_names)
# main()


#Ex.165


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
#
# def main():
#
#     start_y = int(input("Start Year: "))
#     end_y = int(input("End Year: "))
#
#     boys_name = {}
#     girls_name = {}
#
#     for year in range(start_y, end_y + 1):
#         g_fname = "../Unit7_Files_and_exeptions/BabyNames/" + str(year) + "_GirlsNames.txt"
#         b_fname = "../Unit7_Files_and_exeptions/BabyNames/" + str(year) + "_BoysNames.txt"
#
#         addNames(g_fname, girls_name)
#         addNames(b_fname, boys_name)
#
#     print(f"Girl's names that reached #1 in time period {start_y} to {end_y}:")
#     for name in girls_name:
#         print(" ", name)
#     print()
#     print(f"Boys's names that reached #1 in time period {start_y} to {end_y}:")
#     for name in boys_name:
#         print(" ", name)
# main()