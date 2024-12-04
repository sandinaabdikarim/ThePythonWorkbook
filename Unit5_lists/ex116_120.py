#Ex.116

# def properDivisors(n):
#     data_div = []
#
#     for i in range(1,n):
#         if n % i == 0:
#             data_div.append(i)
#
#     return data_div
#
# def perfectDivisors(data, n):
#
#     sum_num = 0
#     is_perfect = False
#     for i in data:
#         sum_num += i
#
#     if sum_num == n:
#         is_perfect = True
#
#     return is_perfect
#
# def main():
#     num = int(input('Enter a number: '))
#     data = properDivisors(num)
#     num_perfect = perfectDivisors(data, num)
#     print(data)
#     print(num_perfect)
# main()

#Ex.117

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
#     string = str(input("Enter a sentence: "))
#     print(onlyWords(string))
#
# main()


#Ex.118

# def wordByWord(data):
#     is_palindrome = False
#
#     rev_data = data.copy()
#     rev_data.reverse()
#     for i in range(len(data)):
#         if data[i] == rev_data[i]:
#             is_palindrome = True
#         else:
#             is_palindrome = False
#
#     return is_palindrome
#
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
#
#     sentence = str(input("Enter a sentence: "))
#     sentence = sentence.lower()
#     list = onlyWords(sentence)
#     result = wordByWord(list)
#     print(result)
#
# main()


#Ex.119

# line = str(input("Enter a number: "))
# data = []
#
# sum_num = 0
# while line != '':
#     num = int(line)
#     data.append(num)
#     line = str(input("Enter a number: "))
#     sum_num += num
#
# average = sum_num / len(data)
# ave_data = []
# above_ave_data = []
#
# for i in data:
#     if i == average:
#         ave_data.append(i)
#     elif i > average:
#         above_ave_data.append(i)
#
# print(data)
# print(average)
# print(ave_data)
# print(above_ave_data)


#Ex.120

# def formattingList(data):
#
#     res = ''
#     for i in range(len(data)):
#         if 0 < i < len(data) - 1 :
#             res += ', ' + data[i]
#         elif i == len(data) - 1:
#             res += ' and ' + data[i]
#         else:
#             res += data[i]
#
#     return res
#
# def main():
#     words = str(input("Enter words: "))
#     values = []
#
#     while words != '':
#         values.append(words)
#         words = str(input("Enter words: "))
#
#     result = formattingList(values)
#     print(result)
#
# main()

