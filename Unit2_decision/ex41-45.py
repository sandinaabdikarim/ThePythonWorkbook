#Ex.41

#side_1 = int(input("Enter the first side of triangle: "))
#side_2 = int(input("Enter the second side of triangle: "))
#side_3 = int(input("Enter the third side of triangle: "))

#if side_1 == side_2 and side_1 == side_3:
#    print("It's a equilateral triangle")
#elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
#    print("It's a isosceles triangle")
#else:
#    print("It's a scalene triangle")


#Ex.42

#C4_freq = 261.63
#D4_freq = 293.66
#E4_freq = 329.63
#F4_freq = 349.23
#G4_freq = 392.00
#A4_freq = 440.00
#B4_freq = 493.88

#name = input("Enter a name of note, for example C4: ")

#note = name[0]
#octave = int(name[1])

#if note == "C":
#    freq = C4_freq
#elif note == "D":
#    freq = D4_freq
#elif note == "E":
#    freq = E4_freq
#elif note == "F":
#    freq = F4_freq
#elif note == "G":
#    freq = G4_freq
#elif note == "A":
#    freq = A4_freq
#elif note == "B":
#    freq = B4_freq

#freq = freq / 2 ** (4 - octave)
#print("The frequency of", name, "is", freq)


#Ex.43

#C4_freq = 261.63
#D4_freq = 293.66
#E4_freq = 329.63
#F4_freq = 349.23
#G4_freq = 392.00
#A4_freq = 440.00
#B4_freq = 493.88

#freq = float(input("Enter the frequency of the note in Hz: "))

#if freq == C4_freq or freq == (C4_freq - 1) or freq == (C4_freq + 1):
#    print("The note is C4")
#elif freq == D4_freq or freq == (D4_freq - 1) or freq == (D4_freq + 1):
#    print("The note is D4")
#elif freq == E4_freq or freq == (E4_freq - 1) or freq == (E4_freq + 1):
#    print("The note is E4")
#elif freq == F4_freq or freq == (F4_freq - 1) or freq == (F4_freq + 1):
#    print("The note is F4")
#elif freq == G4_freq or freq == (G4_freq - 1) or freq == (G4_freq + 1):
#    print("The note is G4")
#elif freq == A4_freq or freq == (A4_freq - 1) or freq == (A4_freq + 1):
#    print("The note is A4")
#elif freq == B4_freq or freq == (B4_freq - 1) or freq == (B4_freq + 1):
#    print("The note is B4")
#else:
#    print("The frequency is not valid")


#Ex.44

#amount = int(input("Enter the denomination of banknote in dollars: "))

#if amount == 1:
#    print("The individual in the banknote is George Washington")
#elif amount == 2:
#    print("The individual in the banknote is Thomas Jefferson")
#elif amount == 5:
#    print("The individual in the banknote is Abraham Lincoln")
#elif amount == 10:
#    print("The individual in the banknote is Alexander Hamilton")
#elif amount == 20:
#    print("The individual in the banknote is Andrew Jackson")
#elif amount == 50:
#    print("The individual in the banknote is Ulysses S. Grant")
#elif amount == 100:
#    print("The individual in the banknote is Benjamin Franklin")
#else:
#    print("The value is wrong")


#Ex.45

#month = str(input('Enter a month: '))
#month = month.title()
#day = int(input('Enter a day: '))

#if month == 'January' and day == 1:
#    print("Holiday is New Year's day")
#elif month == 'July' and day == 1:
#    print("Holiday is Canada Day")
#elif month == 'December' and day == 25:
#    print("Holiday is Christmas Day")
#else:
#    print("The entered month and day do not correspond to a fixed-date holiday")


