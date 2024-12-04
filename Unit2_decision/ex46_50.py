#Ex.46
from audioop import ratecv

#position = str(input("Enter the position of chess board, for example a1: "))
#letter = position[0]
#number = int(position[1])


#if letter == ("a" or letter == "c" or letter == "e" or letter == "g") and number % 2 == 1:
#    print("The square is black")
#elif letter == ("b" or letter == "d" or letter == "f"  or letter == "h") and number % 2 == 0:
#    print("The square is black")
#else:
#    print("The square is white")


#Ex.47

#month = str(input("Enter a month: "))
#month = month.title()
#day = int(input("Enter a day: "))

#if month == "January" or month == "February":
#    print("It's winter")
#elif month == "March":
#    if day < 20:
#        print("It's winter")
#    else:
#        print("It's spring")
#elif month == "April" or month == "May" :
#    print("It's spring")
#elif month == "June":
#    if day < 21:
#        print("It's spring")
#    else:
#        print("It's summer")
#elif month == "July" or month == "August":
#    print("It's summer")
#elif month == "September":
#    if day < 22:
#        print("It's summer")
#    else:
#        print("It's autumn")
#elif month == "October" or month == "November":
#    print("It's autumn")
#elif month == "December":
#    if day < 21:
#        print("It's autumn")
#    else:
#        print("It's winter")


#Ex.48

#month = str(input("Enter a month: "))
#month = month.title()
#day = int(input("Enter a day: "))

#if (month == "December"  and day >= 22) or (month == "January" and day <= 19):
#    print("Your zodiac sign is Capricorn")
#elif (month == "January" and day >= 20) or (month == "February" and day <= 18):
#    print("Your zodiac sign is Aquarius")
#elif (month == "February" and day >= 19) or (month == "March" and day <= 20):
#    print("Your zodiac sign is Pisces")
#elif (month == "March" and day >= 21) or (month == "April" and day <= 19):
#    print("Your zodiac sign is Aries")
#elif (month == "April" and day >= 20) or (month == "May" and day <= 20):
#    print("Your zodiac sign is Taurus")
#elif (month == "May" and day >= 21) or (month == "June" and day <= 20):
#    print("Your zodiac sign is Gemini")
#elif (month == "June" and day >= 21) or (month == "July" and day <= 22):
#    print("Your zodiac sign is Cancer")
#elif (month == "July" and day >= 23) or (month == "August" and day <= 22):
#    print("Your zodiac sign is Leo")
#elif (month == "August" and day >= 23) or (month == "September" and day <= 22):
#    print("Your zodiac sign is Virgo")
#elif (month == "September" and day >= 23) or (month == "October" and day <= 22):
#    print("Your zodiac sign is Libra")
#elif (month == "October" and day >= 23) or (month == "November" and day <= 21):
#    print("Your zodiac sign is Scorpio")
#else:
#    print("Your zodiac sign is Sagittarius")


#Ex.49

# dragon = 2000
# snake = 2001
# horse = 2002
# sheep = 2003
# monkey = 2004
# roostery = 2005
# dog = 2006
# pig = 2007
# rat = 2008
# ox = 2009
# tiger = 2010
# hare = 2011

#year = int(input("Enter a year: "))


# if year < 2000:
#     if (dragon - year) % 12 == 0:
#         print("Your animal is Dragon")
#     elif (snake - year) % 12 == 0:
#         print("Your animal is Snake")
#     elif (horse - year) % 12 == 0:
#         print("Your animal is Horse")
#     elif (sheep - year) % 12 == 0:
#         print("Your animal is Sheep")
#     elif (monkey - year) % 12 == 0:
#         print("Your animal is Monkey")
#     elif (roostery - year) % 12 == 0:
#         print("Your animal is Roostery")
#     elif (dog - year) % 12 == 0:
#         print("Your animal is Dog")
#     elif (pig - year) % 12 == 0:
#         print("Your animal is Pig")
#     elif (rat - year) % 12 == 0:
#         print("Your animal is Rat")
#     elif (ox - year) % 12 == 0:
#         print("Your animal is Ox")
#     elif (tiger - year) % 12 == 0:
#         print("Your animal is Tiger")
#     elif (hare - year) % 12 == 0:
#         print("Your animal is Hare")
# else:
#     if (year - dragon) % 12 == 0:
#         print("Your animal is Dragon")
#     elif (year - snake) % 12 == 0:
#         print("Your animal is Snake")
#     elif (year - horse) % 12 == 0:
#         print("Your animal is Horse")
#     elif (year - sheep) % 12 == 0:
#         print("Your animal is Sheep")
#     elif (year - monkey) % 12 == 0:
#         print("Your animal is Monkey")
#     elif (year - roostery) % 12 == 0:
#         print("Your animal is Roostery")
#     elif (year - dog) % 12 == 0:
#         print("Your animal is Dog")
#     elif (year - pig) % 12 == 0:
#         print("Your animal is Pig")
#     elif (year - rat) % 12 == 0:
#         print("Your animal is Rat")
#     elif (year - ox) % 12 == 0:
#         print("Your animal is Ox")
#     elif (year - tiger) % 12 == 0:
#         print("Your animal is Tiger")
#     elif (year - hare) % 12 == 0:
#         print("Your animal is Hare")


#another solution

# if year % 12 == 8:
#     print("Your animal is Dragon")
# elif year % 12 == 9:
#     print("Your animal is Snake")
# elif year % 12 == 10:
#     print("Your animal is Horse")
# elif year % 12 == 11:
#     print("Your animal is Sheep")
# elif year % 12 == 0:
#     print("Your animal is Monkey")
# elif year % 12 == 1:
#     print("Your animal is Roostery")
# elif year % 12 == 2:
#     print("Your animal is Dog")
# elif year % 12 == 3:
#     print("Your animal is Pig")
# elif year % 12 == 4:
#     print("Your animal is Rat")
# elif year % 12 == 5:
#     print("Your animal is Ox")
# elif year % 12 == 6:
#     print("Your animal is Tiger")
# elif year % 12 == 7:
#     print("Your animal is Hare")



#Ex.50

# magnitude = float(input("Enter a magnitude: "))
#
# if magnitude < 2.0:
#     print(f"Magnitude {magnitude} earthquake is considered to be a Micro earthquake.")
# elif 2.0 <= magnitude < 3.0:
#     print(f"Magnitude {magnitude} earthquake is considered to be a Very Minor earthquake.")
# elif 3.0 <= magnitude < 4.0:
#     print(f"Magnitude {magnitude} earthquake is considered to be a Minor earthquake.")
# elif 4.0 <= magnitude < 5.0:
#     print(f"Magnitude {magnitude} earthquake is considered to be a Light earthquake.")
# elif 5.0 <= magnitude < 6.0:
#     print(f"Magnitude {magnitude} earthquake is considered to be a Moderate earthquake.")
# elif 6.0 <= magnitude < 7.0:
#     print(f"Magnitude {magnitude} earthquake is considered to be a Strong earthquake.")
# elif 7.0 <= magnitude < 8.0:
#     print(f"Magnitude {magnitude} earthquake is considered to be a Major earthquake.")
# elif 8.0 <= magnitude < 10.0:
#     print(f"Magnitude {magnitude} earthquake is considered to be a Great earthquake.")
# elif magnitude >= 10.0:
#     print(f"Magnitude {magnitude} earthquake is considered to be a Meteoric earthquake.")