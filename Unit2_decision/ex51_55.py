#Ex.51
# from math import sqrt
#
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
#
# descriminant = b ** 2 - 4 * a * c
# print(descriminant)
#
# if descriminant > 0:
#     root1 = (-b + sqrt(descriminant)) / (2 * a)
#     root2 = (-b - sqrt(descriminant)) / (2 * a)
#     print(f"The function has two roots: root1: {root1}, root2: {root2}")
# elif descriminant == 0:
#     root1 = -b / (2 * a)
#     print(f"The function has one root: {root1}")
# else:
#     print(f"The function does not have any roots")


#Ex.52

# letter_grade = str(input('Enter a letter grade: '))
# letter_grade = letter_grade.title()
#
# if letter_grade == 'A+':
#     print("Grade points: 4.0")
# elif letter_grade == 'A':
#     print("Grade points: 4.0")
# elif letter_grade == 'A-':
#     print("Grade points: 3.7")
# elif letter_grade == 'B+':
#     print("Grade points: 3.3")
# elif letter_grade == 'B':
#     print("Grade points: 3.0")
# elif letter_grade == 'B-':
#     print("Grade points: 2.7")
# elif letter_grade == 'C+':
#     print("Grade points: 2.3")
# elif letter_grade == 'C':
#     print("Grade points: 2.0")
# elif letter_grade == 'C-':
#     print("Grade points: 1.7")
# elif letter_grade == 'D+':
#     print("Grade points: 1.3")
# elif letter_grade == 'D':
#     print("Grade points: 1.0")
# elif letter_grade == 'F':
#     print("Grade points: 0")
# else:
#     print("Error! Invalid letter grade.")


#Ex.53

# grade_points = float(input("Enter your grade points: "))
#
# if grade_points == 4.0:
#     print("Your letter grade is A+")
# elif grade_points > 3.7:
#     print("Your letter grade is A")
# elif 3.5 < grade_points <= 3.7:
#     print("Your letter grade is A-")
# elif 3.3 <= grade_points < 3.5:
#     print("Your letter grade is B+")
# elif 3.0 <= grade_points < 3.3:
#     print("Your letter grade is B")
# elif 2.7 <= grade_points < 3.0:
#     print("Your letter grade is B-")
# elif 2.3 <= grade_points < 2.7:
#     print("Your letter grade is C+")
# elif 2.0 <= grade_points < 2.3:
#     print("Your letter grade is C")
# elif 1.7 <= grade_points < 2.0:
#     print("Your letter grade is C-")
# elif 1.3 <= grade_points < 1.7:
#     print("Your letter grade is D+")
# elif 1.0 <= grade_points < 1.3:
#     print("Your letter grade is D")
# elif 0 <= grade_points < 1.0:
#     print("Your letter grade is F")
# else:
#     print("Error! Invalid grade points.")


#Ex.54

# rate = float(input('Enter a rate: '))
#
# if rate == 0.0:
#     print("You have Unacceptable Performance")
#     print(f"The amount of employee's raise is {rate * 2400} USA dollars")
# elif rate == 0.4:
#     print("You have Acceptable Performance")
#     print(f"The amount of employee's raise is {rate * 2400} USA dollars")
# elif rate == 0.6:
#     print("You have Meritorious Performance")
#     print(f"The amount of employee's raise is {rate * 2400} USA dollars")
# else:
#     print("Error! Invalid rate.")


#Ex.55

# wavelength = int(input("Enter the wavelength in nanometers: "))
#
# if 380 <= wavelength < 450:
#     print("Violet")
# elif 450 <= wavelength < 495:
#     print("Blue")
# elif 495 <= wavelength < 570:
#     print("Green")
# elif 570 <= wavelength < 590:
#     print("Yellow")
# elif 590 <= wavelength < 620:
#     print("Orange")
# elif 620 <= wavelength < 750:
#     print("Red")
# else:
#     print("The wavelength is outside of the visible spectrum")