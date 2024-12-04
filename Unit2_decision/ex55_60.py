#Ex.56
from itertools import filterfalse

# radiation_freq = float(input("Enter the radiation frequency in Hz: "))
#
# if radiation_freq < 3 * 10 ** 9:
#     print("Radio Waves")
# elif radiation_freq == 3 * 10 ** 9 or radiation_freq < 3 * 10 ** 12:
#     print("Microwaves")
# elif radiation_freq == 3 * 10 ** 12 or radiation_freq < 4.3 * 10 ** 14:
#     print("Infrared Light")
# elif radiation_freq == 4.3 * 10 ** 14 or radiation_freq < 7.5 * 10 ** 14:
#     print("Visible Light")
# elif radiation_freq == 7.5 * 10 ** 14 or radiation_freq < 3 * 10 ** 17:
#     print("Ultraviolet Light")
# elif radiation_freq == 3 * 10 ** 17 or radiation_freq < 3 * 10 ** 19:
#     print("X-Rays")
# elif radiation_freq >= 3 * 10 ** 19:
#     print("Gamma Rays")


#Ex.57

# base_plan = 15
# add_min = 0.25
# add_msg = 0.15
# emergency_calls = 0.44
# sale_tax_rate = 0.05

# num_min = int(input("Enter number of minutes: "))
# num_msg = int(input("Enter number of messages: "))
#
# if num_min <= 50 and num_msg <= 50:
#     total_min = 0
#     total_msg = 0
#     sale_tax = (15.00 + emergency_calls) * 0.05
#     total_bill = 15.00 + emergency_calls + sale_tax
# elif num_min > 50 or num_msg > 50:
#     total_min = (num_min - 50) * add_min
#     total_msg = (num_msg - 50) * add_msg
#     sale_tax = (15.00 + emergency_calls + total_min + total_msg) * 0.05
#     total_bill = 15.00 + emergency_calls + total_min + total_msg + sale_tax
#
# print(f"Your total bill:\n\t- base charge: {base_plan:.2f} dollars"
#       f"\n\t - additional minutes charge: {total_min:.2f} dollars"
#       f"\n\t - additional messages charge: {total_msg:.2f} dollars"
#       f"\n\t - emergency calls charge: {emergency_calls:.2f} dollars"
#       f"\n\t - sale tax: {sale_tax:.2f} dollars"
#       f"\n\t - total bill: {total_bill:.2f} dollars")


#Ex.58

# year = int(input("Enter a year: "))
#
# if year % 400 == 0 and year % 100 != 0 or year % 4 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


#Ex.59

# date = str(input("Enter a date in YYYY/MM/DD format: "))
#
# year = int(date[:4])
# month = int(date[5:7])
# day = int(date[8:10])
#
# next_day = ""
# is_leapyear = False
#
# if month == 4 or month == 6 or month == 9 or month == 11:
#     total_days = 30
#     if day == 30:
#         next_day = 1
#         next_month = month + 1
#         next_year = year
#     else:
#         next_day = day + 1
#         next_month = month
#         next_year = year
# elif month == 2:
#     if day == 28:
#         if year % 400 == 0 and year % 100 != 0 or year % 4 == 0:
#             is_leapyear = True
#             next_day = 29
#             next_month = month
#             next_year = year
#         else:
#             next_day = 1
#             next_month = month + 1
#             next_year = year
#     elif day == 29:
#         next_day = 1
#         next_month = month + 1
#         next_year = year
#     else:
#         next_day = day + 1
#         next_month = month
#         next_year = year
# elif month == 12:
#     if day == 31:
#         next_year = year + 1
#         next_month = 1
#         next_day = 1
#     else:
#         next_day = day + 1
#         next_month = month
#         next_year = year
# else:
#     if day == 30:
#         next_day = 1
#         next_month = month + 1
#         next_year = year
#     else:
#         next_day = day + 1
#         next_month = month
#         next_year = year

# print(f"The next date is {next_year}/{next_month}/{next_day}")


#Ex.60

# from math import floor
#
# year = int(input("Enter a year: "))
#
# day_of_the_week = ((year + floor((year - 1) / 4)) - floor((year - 1) / 100) + floor((year - 1) / 400)) % 7
#
# name_of_the_day = ""
#
# if day_of_the_week == 0:
#     name_of_the_day = "Sunday"
# elif day_of_the_week == 1:
#     name_of_the_day = "Monday"
# elif day_of_the_week == 2:
#     name_of_the_day = "Tuesday"
# elif day_of_the_week == 3:
#     name_of_the_day = "Wednesday"
# elif day_of_the_week == 4:
#     name_of_the_day = "Thursday"
# elif day_of_the_week == 5:
#     name_of_the_day = "Friday"
# elif day_of_the_week == 6:
#     name_of_the_day = "Saturday"
# else:
#     print("Invalid input")
#
# print(name_of_the_day)
