#Ex.146

# from random import randrange
#
# def bingoCard():
#     card = {"B": [], "I": [], "N": [], "G": [], "O": []}
#
#     for i in card:
#         for j in range(5):
#             if i == "B":
#                 num = randrange(1, 16)
#                 card[i].append(num)
#             elif i == "I":
#                 num = randrange(16, 31)
#                 card[i].append(num)
#             elif i == "N":
#                 num = randrange(31, 46)
#                 card[i].append(num)
#             elif i == "G":
#                 num = randrange(46, 61)
#                 card[i].append(num)
#             elif i == "O":
#                 num = randrange(61, 76)
#                 card[i].append(num)
#
#     return card
#
# def main():
#     ran_card = bingoCard()
#
#     for i in ran_card:
#         print(i, end='   ')
#
#     print()
#
#     for j in range(5):
#         for i in ran_card.keys():
#             print (ran_card[i][j], end='  ')
#         print()
#
# main()


#Ex.147

# from random import randrange
#
# def bingoCard():
#     card = {"B": [], "I": [], "N": [], "G": [], "O": []}
#
#     lower = 1
#     upper = 15 + 1
#
#     for letter in card:
#         while len(card[letter]) != 5:
#             num = randrange(lower, upper)
#             if num not in card[letter]:
#                 card[letter].append(num)
#         lower += 15
#         upper += 15
#     return card
#
# def displayCard(card):
#
#     for i in card:
#         print(i, end='   ')
#
#     print()
#
#     for j in range(5):
#         for i in card.keys():
#             print(card[i][j], end='  ')
#         print()
#
# def winnerNumbers():
#     lower = 1
#     upper = 15 + 1
#     win_num = []
#
#     while len(win_num) != 5:
#         num = randrange(lower, upper)
#         if num not in win_num:
#             win_num.append(num)
#         lower += 15
#         upper += 15
#     return win_num
#
# def areYouWinner(card, win_num):
#
#     for i in win_num:
#         for j in card.values():
#             for m in range(len(j)):
#                 if i == j[m]:
#                     j[m] = 0
#
#     sum_v = False
#     sum_g = False
#     sum_d = False
#
#     for l in card.values():
#         list_v= []
#         for n in l:
#             if n == 0:
#                 list_v.append(n)
#             else:
#                 list_v.append(n)
#         if sum(list_v) == 0:
#             sum_v = True
#             return sum_v
#         else:
#             sum_v = False
#
#     for num in range(5):
#         list_g = []
#         for key in card:
#             list_g.append(card[key][num])
#         if sum(list_g) == 0:
#             sum_g = True
#             return sum_g
#         else:
#             sum_g = False
#
#     list_d = []
#
#     for number in range(5):
#         for key_index in range(len(card)):
#             for key_value in card:
#                 if number == key_index:
#                     if card[key_value][number] == 0:
#                         list_d.append(card[key_value][number])
#                         break
#                 else:
#                     break
#     if sum(list_d) == 0 and len(list_d) == 5:
#         sum_d = True
#         return sum_d
#     else:
#         sum_d = False
#
#
#     return False
#
#
# def main():
#     ran_card = bingoCard()
#     win_card_numbers = winnerNumbers()
#     zero_card = areYouWinner(ran_card, win_card_numbers)
#     displayCard(ran_card)
#     print(zero_card)
#     print(win_card_numbers)
#
# main()


#Ex.148

# from random import randrange, shuffle
#
# def bingoCard():
#     card = {"B": [], "I": [], "N": [], "G": [], "O": []}
#
#     lower = 1
#     upper = 15 + 1
#
#     for letter in card:
#         while len(card[letter]) != 5:
#             num = randrange(lower, upper)
#             if num not in card[letter]:
#                 card[letter].append(num)
#         lower += 15
#         upper += 15
#     return card
#
# def displayCard(card):
#
#     for i in card:
#         print(i, end='   ')
#
#     print()
#
#     for j in range(5):
#         for i in card.keys():
#             print(card[i][j], end='  ')
#         print()
#
# def winnerNumbers():
#     lower = 1
#     upper = 15 + 1
#     win_num = []
#
#     while len(win_num) != 5:
#         num = randrange(lower, upper)
#         if num not in win_num:
#             win_num.append(num)
#         lower += 15
#         upper += 15
#     return win_num
#
# def areYouWinner(card, win_num):
#
#     for i in win_num:
#         for j in card.values():
#             for m in range(len(j)):
#                 if i == j[m]:
#                     j[m] = 0
#
#     sum_v = False
#     sum_g = False
#     sum_d = False
#
#     for l in card.values():
#         list_v= []
#         for n in l:
#             if n == 0:
#                 list_v.append(n)
#             else:
#                 list_v.append(n)
#         if sum(list_v) == 0:
#             sum_v = True
#             return sum_v
#         else:
#             sum_v = False
#
#     for num in range(5):
#         list_g = []
#         for key in card:
#             list_g.append(card[key][num])
#         if sum(list_g) == 0:
#             sum_g = True
#             return sum_g
#         else:
#             sum_g = False
#
#     list_d = []
#
#     for number in range(5):
#         for key_index in range(len(card)):
#             for key_value in card:
#                 if number == key_index:
#                     if card[key_value][number] == 0:
#                         list_d.append(card[key_value][number])
#                         break
#                 else:
#                     break
#     if sum(list_d) == 0 and len(list_d) == 5:
#         sum_d = True
#         return sum_d
#     else:
#         sum_d = False
#
#
#     return False
#
# def main():
#     ran_card = bingoCard()
#     win_card_numbers = winnerNumbers()
#     zero_card = areYouWinner(ran_card, win_card_numbers)
#     displayCard(ran_card)
#     print(zero_card)
#     print(win_card_numbers)
#
# main()

