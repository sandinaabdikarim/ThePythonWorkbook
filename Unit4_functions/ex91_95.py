#Ex.91

# def ordinalDate(day, month, year):
#     ordinal_day = 0
#     if year % 400 == 0 and year % 100 != 0 or year % 4 == 0:
#         is_leap_year = True
#     else:
#         is_leap_year = False
#
#     for i in range(1, month):
#         if i == 2:
#             if is_leap_year:
#                 total_days = 29
#                 ordinal_day += total_days
#             else:
#                 total_days = 28
#                 ordinal_day += total_days
#         if i == 4 or i == 6 or i == 9 or i == 11:
#             total_days = 30
#             ordinal_day += total_days
#         elif i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
#             total_days = 31
#             ordinal_day += total_days
#     ordinal_day += day
#     return ordinal_day
#
# def main():
#     date = str(input("Enter a date in DD/MM/YYYY: "))
#     day = int(date[0:2])
#     month = int(date[3:5])
#     year = int(date[6:])
#
#     print(f"{year} - {ordinalDate(day, month, year)}")
#
# main()


#Ex.92

# def ordinalDate(ord_d, year):
#     day = 0
#     month = 0
#     if year % 400 == 0 and year % 100 != 0 or year % 4 == 0:
#         is_leap_year = True
#         total_days = 366
#     else:
#         is_leap_year = False
#         total_days = 365
#
#     all_months = "31 28 30"
#
#     for i in range(1, 13):
#         if (i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12) and ord_d >= 31:
#             if ord_d == 31:
#                 day = ord_d
#                 month = i
#                 break
#             else:
#                 ord_d -= int(all_months[0:2])
#                 month += 1
#         elif i == 2 and ord_d >= 29:
#             if ord_d == 29 and is_leap_year:
#                 day = ord_d
#                 month = i
#                 break
#             else:
#                 if is_leap_year:
#                     ord_d -= (int(all_months[3:5]) + 1)
#                     month += 1
#                 else:
#                     ord_d -= int(all_months[3:5])
#                     month += 1
#         elif (i == 4 or i == 6 or i == 9 or i == 11) and ord_d >= 30:
#             if ord_d == 30:
#                 day = ord_d
#                 month = i
#                 break
#             else:
#                 ord_d -= int(all_months[6:])
#                 month += 1
#         elif 0 < ord_d < 31:
#             day = ord_d
#             ord_d -= day
#             month += 1
#             break
#     return day, month
#
# def main():
#     date = str(input("Enter a date in YYYY - ordinal date: "))
#     year = int(date[0:4])
#     ordinal_date = int(date[5:])
#
#     print(ordinalDate(ordinal_date, year))
#
# main()


#Ex.93

# def centerString(s, width):
#     if width < len(s):
#         return s
#     else:
#         space =  (width - len(s)) // 2
#         result = "." * space + s
#         return result
#
# def main():
#     line = str(input("Enter the string: "))
#
#     while line != '':
#         w = int(input("Enter the width: "))
#         print(centerString(line, w))
#         line = str(input("Enter the string: "))
#
# main()


#Ex.94

# def isTriangle(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return False
#     mx = max(a, b, c)
#     mn = min(a, b, c)
#     md = (a + b + c) - mx - mn
#
#     if mx >= (mn + md):
#         return False
#
#     return True
#
# def main():
#     x = int(input("Enter length of straw a: "))
#     y = int(input("Enter length of straw b: "))
#     z = int(input("Enter length of straw c: "))
#
#     print(isTriangle(x, y, z))
#
# main()


#Ex.95

# def capitalizeIt(s):
#     new_s = ""
#     for i in range(len(s)):
#         if i == 0 and s[i] != " ":
#             new_s += s[i].upper()
#         elif s[i - 1] == " " and (s[i - 2] == "." or s[i - 2] == "!" or s[i - 2] == "?"):
#             new_s += s[i].upper()
#         elif s[i - 1] == "." or s[i - 1] == "!" or s[i - 1] == "?":
#             new_s += s[i].upper()
#         elif s[i] == "i" and s[i - 1] == " " and (s[i + 1] == " " or s[i + 1] == "’"):
#             new_s += s[i].upper()
#         else:
#             new_s += s[i]
#
#     return new_s
#
# def main():
#     string = input("Enter a string: ")
#
#     result = capitalizeIt(string)
#     print(result)
#
# main()


