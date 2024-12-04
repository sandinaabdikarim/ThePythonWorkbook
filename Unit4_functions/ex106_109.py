#Ex.106

# def daysInMonth(year, month):
#
#     is_leap_year = False
#
#     if year % 400 == 0 and year % 100 != 0 or year % 4 == 0:
#         is_leap_year = True
#
#     if month == 4 or month == 6 or month == 9 or month == 11:
#         days = 30
#     elif month == 2:
#         if is_leap_year:
#             days = 29
#         else:
#             days = 28
#     else:
#         days = 31
#
#     return days
#
# def main():
#     m = int(input("Enter a month(1-12): "))
#     y = int(input("Enter a year: "))
#
#     result = daysInMonth(y, m)
#     print(result)
# main()


#Ex.107

# def reduceFraction(numerator, denominator):
#
#     GCD = min(numerator, denominator)
#
#     while numerator % GCD != 0 or denominator % GCD != 0:
#         GCD -= 1
#
#     red_num = numerator // GCD
#     red_denom = denominator // GCD
#     return red_num, red_denom
#
# def main():
#     n = int(input("Enter a numerator: "))
#     d = int(input("Enter a denominator: "))
#
#     result = reduceFraction(n, d)
#     print(result)
# main()

#Ex.108

# def reduceMeasures(volume, measure):
#     CUP_T = 16
#     TAB_TEA = 3
#     cups = 0
#     tablespoons = 0
#     teaspoons = 0
#
#     if measure == 'cup' or measure == 'cups':
#         return f"It is already the largest unit of measure"
#     if measure == 'tableaspoon' or measure == 'tablespoons':
#         while volume != 0:
#             cups = volume // CUP_T
#             volume = volume % CUP_T
#             if volume < 16:
#                 tablespoons = volume
#                 volume = 0
#         return f"{cups} cup(s), {tablespoons} tablespoon(s)"
#     if measure == 'teaspoon' or measure == 'teaspoons':
#         while volume != 0:
#             cups = volume // (CUP_T * TAB_TEA)
#             volume = volume % (CUP_T * TAB_TEA)
#             if volume < CUP_T * TAB_TEA:
#                 tablespoons = volume // TAB_TEA
#                 volume = volume % TAB_TEA
#             if volume < TAB_TEA:
#                 teaspoons = volume
#                 volume = 0
#         return f"{cups} cup(s), {tablespoons} tablespoon(s), {teaspoons} teaspoon(s)"
#
# def main():
#     vol = int(input("Enter volume: "))
#     mea = input("Enter measure: ")
#     print(reduceMeasures(vol, mea))
# main()


#Ex.109

# def magicDate(d, m, y):
#
#     y = str(y)
#     res = False
#     if d * m == int(y[2:]):
#         res = True
#
#     return res
#
# def daysInMonth(year, month):
#
#     is_leap_year = False
#
#     if year % 400 == 0 and year % 100 != 0 or year % 4 == 0:
#         is_leap_year = True
#
#     if month == 4 or month == 6 or month == 9 or month == 11:
#         days = 30
#     elif month == 2:
#         if is_leap_year:
#             days = 29
#         else:
#             days = 28
#     else:
#         days = 31
#
#     return days
#
# def main():
#     all_dates = ''
#     counts = 0
#     for years in range(1900, 2000):
#         for months in range(1, 13):
#             for days in range(1, daysInMonth(years, months)):
#                 result = magicDate(days, months, years)
#                 if result:
#                     all_dates += str(years) + '-' + str(months) + '-' + str(days) + '\n'
#                     counts += 1
#
#     print(all_dates)
#     print(counts)
# main()

