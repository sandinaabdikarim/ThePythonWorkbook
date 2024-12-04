#Ex.126

# def createDeck():
#     suits = ["c", "d", "h", "s"]
#     num_hearts = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
#     card_deck = []
#
#     for i in suits:
#         for j in num_hearts:
#             card_deck.append((j+i))
#
#     return card_deck
#
# def shuffleCards(cd):
#     from random import randrange
#
#     sh_card_deck = []
#     for card in range(len(cd)):
#         random_card = randrange(card,len(cd))
#         temp = cd[card]
#         cd[card] = cd[random_card]
#         cd[random_card] = temp
#
#     return cd
#
# def deal(h, cph, deck):
#     all_h = ''
#     res_h = ''
#     for i in range(cph):
#         for j in range(h):
#             all_h += deck.pop(j) + ' '
#
#     tmp_data = all_h.split(' ')
#
#     for i in range(h):
#         for j in range(i, len(tmp_data), h):
#             res_h += tmp_data[j] + " "
#         res_h += ","
#
#     data_h = res_h.split(",")
#
#     return data_h, deck
#
# def main():
#     hands = 4
#     card_in_hand = 5
#     cards = createDeck()
#     shuffle_cards = shuffleCards(cards)
#     card_in_hands, remain_deck = deal(hands, card_in_hand, shuffle_cards)
#
#     for i in card_in_hands:
#         print(i)
#     print(remain_deck)
# main()


#Ex.127

# def sortedList(data):
#     is_sorted = False
#
#     mx = max(data)
#     mn = min(data)
#
#     if data[0] == mn:
#         prev = data[0]
#         for i in range(1, len(data)):
#             if data[i] > prev:
#                 prev = data[i]
#                 is_sorted = True
#             else:
#                 is_sorted = False
#                 break
#     elif data[0] == mx:
#         prev = data[0]
#         for i in range(1, len(data)):
#             if data[i] < prev:
#                 prev = data[i]
#                 is_sorted = True
#             else:
#                 is_sorted = False
#                 break
#
#     return is_sorted
#
# def main():
#
#     num = str(input("Enter a number: "))
#     list = []
#     while num != "":
#         num = int(num)
#         list.append(num)
#         num = str(input("Enter a number: "))
#
#     result = sortedList(list)
#     print(result)
# main()


#Ex.128

# def countRange(data, mn, mx):
#     count = 0
#
#     for i in data:
#         if i >= mn and i <= mx:
#             count += 1
#     return count
#
# def main():
#     list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     print("Result: %d Expected: 2" % countRange(list, 5, 7))
#     print("Result: %d Expected: 10" % countRange(list, -5, 77))
#     print("Result: %d Expected: 0" % countRange(list, 12, 17))
#
# main()


#Ex.129

# def tokenizingString(s):
#     s = s.replace(' ', '')
#
#     token = []
#     i = 0
#     operators = '*/+-()'
#     numbers = '0123456789'
#     while i < len(s):
#         if s[i] in operators:
#             token.append(s[i])
#             i += 1
#         elif s[i] in numbers:
#             num = ''
#             while i < len(s) and s[i] in numbers:
#                 num += s[i]
#                 i += 1
#             token.append(num)
#         else:
#             return []
#     return token
#
# def main():
#     exp = input('Enter an expression: ')
#     tokens = tokenizingString(exp)
#     print(tokens)
# main()


#Ex.130

# def tokenizingString(s):
#     s = s.replace(' ', '')
#
#     token = []
#     u_token = []
#     i = 0
#     operators = '*/+-()'
#     numbers = '0123456789'
#     while i < len(s):
#         if s[i] in operators:
#             token.append(s[i])
#             i += 1
#         elif s[i] in numbers:
#             num = ''
#             while i < len(s) and s[i] in numbers:
#                 num += s[i]
#                 i += 1
#             token.append(num)
#         else:
#             return []
#     return token
#
# def unaryOperators(tokens):
#     operators = '*/+-()'
#     data = tokens.copy()
#
#     for i in range(len(data)):
#         if i == 0:
#             if data[i] == "+":
#                 data[i] = "u+"
#             elif data[i] == "-":
#                 data[i] = "u-"
#         else:
#             if data[i] == "+" and data[i-1] in operators:
#                 data[i] = "u+"
#             elif data[i] == "-" and data[i-1] in operators:
#                 data[i] = "u-"
#     return data
#
#
# def main():
#     exp = input('Enter an expression: ')
#     tokens = tokenizingString(exp)
#     u_tokens = unaryOperators(tokens)
#
#     una_oper = []
#     for i in u_tokens:
#         if i == "u-" or i == "u+":
#             una_oper.append(i)
#
#     print(tokens)
#     print(una_oper)
# main()