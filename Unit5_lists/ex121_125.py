#Ex.121
from multiprocessing.managers import convert_to_error

# from random import randint
#
# data = []
# counter = 0
#
# while counter != 6:
#     num = randint(1, 50)
#     if num not in data:
#         data.append(num)
#         counter += 1
#
# data.sort()
# print(data)


#Ex.122

# line = str(input("Enter a word: "))
#
# vowels = 'aeiou'
# consonants = 'bcdfghjklmnpqrstvwxyz'
#
# line = line.lower()
# data = []
# pig_latin = ''
# tmp = ''
# counter = 0
#
# if line[0] in vowels:
#     pig_latin += line + "way"
# elif line[0] in consonants:
#     while line[counter] not in vowels and counter < len(line) - 1:
#         tmp += line[counter]
#         counter += 1
#
#     for i in range(counter, len(line)):
#         data.append(line[i])
#     for i in range(0, len(tmp)):
#         data.append(tmp[i])
#     data.append("a")
#     data.append("y")
#
#     for i in range(0, len(data)):
#         pig_latin += data[i]
#
# print(pig_latin)


#Ex.123

# line = str(input("Enter a word: "))
#
# vowels = 'aeiou'
# consonants = 'bcdfghjklmnpqrstvwxyz'
# marks = "!,.?"
#
# line = line.lower()
# data = []
# pig_latin = ''
# tmp = ''
# tmp_marker = ''
# counter = 0
#
# for i in line:
#     if i in marks:
#         tmp_marker += i
#     else:
#         data.append(i)
#
# if data[0] in vowels:
#     for i in range(len(data)):
#         pig_latin += data[i]
#     pig_latin += "way" + tmp_marker
#
# elif data[0] in consonants:
#     while data[counter] not in vowels and counter < len(data) - 1:
#         tmp += data[counter]
#         counter += 1
#     for i in range(counter):
#         data.append(tmp[i])
#         data.remove(tmp[i])
#
#     for i in range(len(data)):
#         pig_latin += data[i]
#
#     pig_latin += "ay" + tmp_marker
#
# pig_latin = pig_latin.capitalize()
# print(pig_latin)


#124

# x = str(input("Enter a number x: "))
#
# data_x = []
# data_y = []
# n = 0
# while x != '':
#     y = float(input("Enter a number y: "))
#     data_x.append(float(x))
#     data_y.append(y)
#     n += 1
#     x = str(input("Enter a number x: "))
#
# m_part1 = 0
# m_part2_x = 0
# m_part2_y = 0
# m_part3 = 0
#
# for i in range(len(data_x)):
#     m_part1 += (data_x[i] * data_y[i])
#     m_part2_x += data_x[i]
#     m_part2_y += data_y[i]
#     m_part3 += data_x[i] ** 2
#
# m = (m_part1 - ((m_part2_x * m_part2_y) / n)) / (m_part3 - ((m_part2_x ** 2) / n))
# b = (m_part2_y / n) - m * (m_part2_x / n)
#
# print(f"{m:.2f}x + {b:.1f}")


#Ex.125

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
# def main():
#     cards = createDeck()
#     print(cards)
#     shuffle_cards = shuffleCards(cards)
#     print(shuffle_cards)
# main()

