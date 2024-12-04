#Ex.63

# number = int(input("Enter a number (0 to quit): "))
# count_sum = 0
# count_num = 0
# if number == 0:
#     print("Invalid the first input. Try again.")
# else:
#     while number != 0:
#         count_sum = count_sum + number
#         count_num += 1
#         number = int(input("Enter a number (0 to quit): "))
#
#     print(f'Average of values {count_sum / count_num}')


#Ex.64

# discount = 0.6
# old_price = 4.95
# while old_price <= 24.95:
#     discounted_price = old_price * discount
#     new_price = old_price - discounted_price
#     print(old_price)
#     print(f"Discount amount: {discounted_price:.2f}, new price: {new_price:.2f}")
#     old_price = old_price + 5


#Ex.65

# for i in range(0, 110, 10):
#     t_fahrenheit = (i * 9 / 5) + 32
#     print(f"Temperature in Celsius: {i} \nTemperature in Fahrenheit: {t_fahrenheit}")


#Ex.66

# price = str(input("Enter a price: "))
#
# total_amount = 0.00
# while price != '':
#     total_amount = total_amount + float(price)
#     price = str(input("Enter a price: "))
#
# payment = str(input("Do you pay by cash or card?: "))
# payment = payment.lower()
#
# if payment == 'cash':
#     remainder = total_amount * 100 % 5
#     if remainder < 2.5:
#         cash_total = total_amount - remainder / 100
#         print("The cash amount payable is %.02f" % cash_total)
#     else:
#         cash_total = total_amount + 0.05 - remainder / 100
#         print("The cash amount payable is %.02f" % cash_total)
# else:
#     print(total_amount)


#Ex.67
# from math import sqrt
#
# first_x = int(input("Enter the first x-coordinate: "))
# first_y = int(input("Enter the first y-coordinate: "))
#
# prev_x = first_x
# prev_y = first_y
#
# perimeter = 0
#
# line = str(input("Enter the next x-coordinate (blank to quit): "))
# while line != '':
#     x = int(line)
#     y = int(input("Enter the next y-coordinate: "))
#     distance = sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2)
#     perimeter += distance
#     prev_x = x
#     prev_y = y
#     line = str(input("Enter the next x-coordinate (blank to quit): "))
#
# distance = sqrt((first_x - x) ** 2 + (first_y - y) ** 2)
# perimeter += distance
#
# print("The perieter of that polygon is ",perimeter)

#Ex.68

# letter_grade = str(input("Enter a letter grade: "))
# letter_grade = letter_grade.upper()
#
# letter_count = 0
# sum_grades = 0.0
#
# while letter_grade != '':
#     letter_count += 1
#
#     if letter_grade == 'A+':
#         sum_grades += 4.0
#     elif letter_grade == 'A':
#         sum_grades += 4.0
#     elif letter_grade == 'A-':
#         sum_grades += 3.7
#     elif letter_grade == 'B+':
#         sum_grades += 3.3
#     elif letter_grade == 'B':
#         sum_grades += 3.0
#     elif letter_grade == 'B-':
#         sum_grades += 2.7
#     elif letter_grade == 'C+':
#         sum_grades += 2.3
#     elif letter_grade == 'C':
#         sum_grades += 2.0
#     elif letter_grade == 'C-':
#         sum_grades += 1.7
#     elif letter_grade == 'D+':
#         sum_grades += 1.3
#     elif letter_grade == 'D':
#         sum_grades += 1.0
#     elif letter_grade == 'F':
#         sum_grades += 0.0
#
#     letter_grade = str(input("Enter a letter grade: ")).upper()
#
# average = sum_grades / letter_count
# print(average)


#Ex.69

# age = str(input('Enter the guest age: '))
#
# admission_cost = 0
#
# while age != '':
#     age = int(age)
#     if age <= 2:
#         admission_cost += 0
#     elif 3 < age < 12:
#         admission_cost += 14
#     elif age >= 65:
#         admission_cost += 18
#     else:
#         admission_cost += 23
#
#     age = str(input('Enter a guest age: '))
#
# print("The total admission cost for the group is %.02f" % admission_cost)


#Ex.70

# line = str(input("Enter 8 bits: "))
#
# while line != '':
#     if line.count("0") + line.count("1") != 8 or len(line) != 8:
#         print("That wasn't 8 bits.. Try again.")
#     else:
#         ones = line.count("1")
#         if ones % 2 == 0:
#             print("The parity bit should be 0")
#         else:
#             print("The parity bit should be 1")
#
#     line = str(input("Enter 8 bits: "))