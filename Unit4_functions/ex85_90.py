#Ex.85
# from math import sqrt
#
# def hypotenuse(a, b):
#     c = sqrt(a**2 + b**2)
#     return c
#
# def main():
#     a = int(input("Enter a length of a-side: "))
#     b = int(input("Enter a length of b-side: "))
#
#     c = hypotenuse(a, b)
#     print("The hypotenuse is", c)
#
# main()


#Ex.86


# base_fare = 4.00
# for_meters = 0.25
#
# def totalFare(distance):
#     total_amount = base_fare + for_meters * (distance * 1000 // 140)
#     return total_amount
#
# def main():
#     distance = int(input("Enter distance in kms: "))
#     total_amount = totalFare(distance)
#     print("Your total fare is ", total_amount, "dollars")
#
# main()


#Ex.87

# first_item = 10.95
# other_items = 2.95
#
# def totalCharge(num):
#     total_amount = first_item  + (other_items * (num -1))
#     return total_amount
#
# def main():
#     num_items = int(input("Enter the number of items: "))
#     total_charge = totalCharge(num_items)
#     print("Your total charge is", total_charge, "dollars")
#
# main()


#Ex.88

# def medianValue(a, b, c):
#     mx = max(a, b, c)
#     mn = min(a, b, c)
#     sum_three = a + b + c
#     median_value = (sum_three - mx - mn) / 2
#     return median_value
#
# def main():
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     c = int(input("Enter the third number: "))
#     print(medianValue(a, b, c))
#
# main()


#Ex.89

# def ordinalNumbers(num):
#     if 1 < num > 12:
#         return ""
#     else:
#         if num == 1:
#             return "1 - first"
#         elif num == 2:
#             return "2 - second"
#         elif num == 3:
#             return "3 - third"
#         elif num == 4:
#             return "4 - fourth"
#         elif num == 5:
#             return "5 - fifth"
#         elif num == 6:
#             return "6 - sixth"
#         elif num == 7:
#             return "7 - seventh"
#         elif num == 8:
#             return "8 - eighth"
#         elif num == 9:
#             return "9 - ninth"
#         elif num == 10:
#             return "10 - tenth"
#         elif num == 11:
#             return "11 - eleventh"
#         elif num == 12:
#             return "12 - twelfth"
#
# def main():
#     number = int(input("Enter a number from 1 to 12: "))
#     print(ordinalNumbers(number))
#
# main()


#Ex.90

# def ordinalNumbers(num):
#     if 1 < num > 12:
#         return ""
#     else:
#         if num == 1:
#             return "first"
#         elif num == 2:
#             return "second"
#         elif num == 3:
#             return "third"
#         elif num == 4:
#             return "fourth"
#         elif num == 5:
#             return "fifth"
#         elif num == 6:
#             return "sixth"
#         elif num == 7:
#             return "seventh"
#         elif num == 8:
#             return "eighth"
#         elif num == 9:
#             return "ninth"
#         elif num == 10:
#             return "tenth"
#         elif num == 11:
#             return "eleventh"
#         elif num == 12:
#             return "twelfth"
#
#
# def displayVerse(n):
#     print("On the", ordinalNumbers(n), "day in Christmas")
#     print("my true love sent to me:")
#
#     if n >= 12:
#         print("Twelve drummers drumming")
#     if n >= 11:
#         print("Eleven pipers piping")
#     if n >= 10:
#         print("Ten lords a-leaping")
#     if n >= 9:
#         print("Nine ladies dancing")
#     if n >= 8:
#         print("Eight maids a-milking")
#     if n >= 7:
#         print("Seven swans a-swimming")
#     if n >= 6:
#         print("Six geese a-laying")
#     if n >= 5:
#         print("Five gold rings")
#     if n >= 4:
#         print("Four calling birds")
#     if n >= 3:
#         print("Three french hens")
#     if n >= 2:
#         print("Two turtle doves")
#     if n == 1:
#         print("A", end=" ")
#     else:
#         print("And a", end=" ")
#     print("partridge in a pear tree")
#     print()
#
# def main():
#     for verse in range(1, 13):
#         displayVerse(verse)
#
# main()

