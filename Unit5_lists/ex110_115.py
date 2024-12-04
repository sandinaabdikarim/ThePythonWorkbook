#Ex.110

# number = int(input('Enter a number (0 to quit): '))
#
# data = []
#
# while number != 0:
#     data.append(number)
#     number = int(input('Enter a number (0 to quit): '))
# data.sort()
# print(data)


#Ex.111

# number = int(input('Enter a number: '))
# data = []
#
# while number != 0:
#     data.append(number)
#     number = int(input('Enter a number: '))
#
# data.sort()
# data.reverse()
#
# for i in data:
#     print(i)


#Ex.112

# def removeMxMn(n):
#
#     for i in range(2):
#         mx = max(n)
#         mn = min(n)
#         n.remove(mx)
#         n.remove(mn)
#
#     data = n
#     return data
#
# def main():
#     numbers = int(input('Enter numbers: '))
#     values = []
#     while numbers != 0:
#         values.append(numbers)
#         numbers = int(input('Enter numbers: '))
#
#     if len(values) <= 4:
#         print("Try again. Need to be larger than 4")
#     else:
#         print(values, "Original list")
#         print(removeMxMn(values), "Removed list")
# main()


#Ex.113

# line = str(input("Enter a word: "))
# data = []
#
# while line != '':
#     if line not in data:
#         data.append(line)
#     line = str(input("Enter a word: "))
#
# for word in data:
#     print(word)


#Ex.114

# number = input('Enter a number: ')
# data = []
# negatives = ''
# positives = ''
# zeroes = ''
#
# while number != '':
#     data.append(number)
#     number = input('Enter a number: ')
# data.sort()
#
# for i in data:
#     if int(i) < 0:
#         negatives += str(i) + " "
#     elif int(i) == 0:
#         zeroes += str(i) + " "
#     else:
#         positives += str(i) + " "
# print(negatives)
# print(zeroes)
# print(positives)


#Ex.115

# def properDivisors(n):
#     data_div = []
#
#     for i in range(1,n):
#         if n % i == 0:
#             data_div.append(i)
#
#     return data_div
#
# def main():
#     num = int(input('Enter a number: '))
#     data = properDivisors(num)
#     print(data)
# main()

