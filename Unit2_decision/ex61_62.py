#Ex.61
from random import random

# license_plate = str(input("Enter a license plate: "))
# license_plate = license_plate.upper()
#
# if license_plate[:3].isalpha() and license_plate[3:].isdigit() and len(license_plate) == 6:
#     print("License plate is old format")
# elif license_plate[:4].isdigit() and license_plate[4:].isalpha() and len(license_plate) == 7:
#     print("License plate is new format")
# else:
#     print("Invalid input")


#Ex.62
# from random import randint
# roulette_wheel = 36
#
# spin_result = randint(0,roulette_wheel)
# print(f"Spin resulted in {spin_result}")
#
# if spin_result == 0:
#     print("Pay Green")
#     print("Pay 0")
#     pass
# elif spin_result > 0:
#     if spin_result == 1 or spin_result == 3 or spin_result == 5 or spin_result == 7 or spin_result == 9 \
#     or spin_result == 12 or spin_result == 14 or spin_result == 16 or spin_result == 18 or \
#         spin_result == 19 or spin_result == 21 or spin_result == 23 or spin_result == 25 or \
#         spin_result == 27 or spin_result == 30 or spin_result == 32 or spin_result == 34 or \
#         spin_result == 36:
#         print("Pay Red")
#         if spin_result % 2 == 0:
#             print("Pay Even")
#         else:
#             print("Pay Odd")
#     else:
#         print("Pay Black")
#         if spin_result % 2 == 0:
#             print("Pay Even")
#         else:
#             print("Pay Odd")
#
# if 1 <= spin_result <= 18:
#     print("Pay 1 to 18")
# elif 19 <= spin_result <= 36:
#     print("Pay 1 to 36")
