#Ex.171

# line_length = 50
# fname = "test171origin.txt"
# inf = open(fname, "r")
# all_lines = []
#
# line = inf.readline()
# while line != "":
#     line = line.rstrip()
#     words = line.split()
#     all_lines += words
#     line = inf.readline()
#
# inf.close()
# w_line = ""
# fname2 = "test171new.txt"
# outf = open(fname2, "w")
#
# for i in range(len(all_lines)):
#     if (len(w_line) + len(all_lines[i])) < line_length:
#         w_line += all_lines[i] + " "
#     else:
#         outf.write(w_line + "\n")
#         w_line = ""
#         w_line += all_lines[i] + " "
# outf.write(w_line + "\n")
#
# outf.close()


#Ex172

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
# def searchVowels(word):
#     vowels = ["a", "e", "i", "o", "u", "y"]
#     isVowelsInOrder = False
#
#     pointer1 = 0
#     pointer2 = 0
#
#     while pointer2 < len(word):
#         if vowels[pointer1] == word[pointer2]:
#             pointer1 += 1
#             pointer2 += 1
#         else:
#             pointer2 += 1
#     if pointer1 == len(vowels):
#         isVowelsInOrder = True
#
#     return isVowelsInOrder
#
# def main():
#
#     fname = input("Enter file name: ")
#     try:
#         inf = open(fname, "r")
#     except FileNotFoundError:
#         print("File not found")
#         quit()
#
#     line = inf.readline()
#     vowels_order = []
#
#     while line != "":
#         line = line.rstrip()
#         res_line = onlyWords(line)
#         for i in res_line:
#             i = i.lower()
#             inorder = searchVowels(i)
#             if inorder:
#                 vowels_order.append(i)
#         line = inf.readline()
#
#     inf.close()
#     print(vowels_order)
# main()

