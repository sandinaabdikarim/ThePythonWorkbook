#Ex.21

#b = int(input("Enter a b: "))
#h = int(input("Enter a h: "))

#area = (b * h) / 2

#print(f'Area of the triangle is {area}')


#Ex.22

#from math import sqrt

#s1 = int(input("Enter a length of the first side: "))
#s2 = int(input("Enter a length of the second side: "))
#s3 = int(input("Enter a length of the third side: "))

#s = (s1 + s2 + s3) / 2
#area = sqrt(s * (s - s1) * (s - s2) * (s - s3))

#print(f'The area of the triangle is {area:.2f}')

#Ex.23

#from math import tan, pi

#s = int(input("Enter a length of a polygon: "))
#n = int(input("Enter a number of sides of a polygon: "))

#area = (n * s ** 2) / 4 * tan(pi/n)
#print("The area of the polygon is", area)


#Ex.24

#days = int(input("Enter number of days: "))
#hours = int(input("Enter number of hours: "))
#minutes = int(input("Enter number of minutes: "))
#seconds = int(input("Enter number of seconds: "))

#total_seconds = days * 24 * 3600 + hours * 3600 + minutes * 60 + seconds
#print(f'Total duration in seconds: {total_seconds}')

#Ex.25

#duration = int(input("Enter duration in seconds: "))

#days = duration // (24 * 3600)
#duration = duration % (24 * 3600)
#hours = duration // 3600
#duration = duration % 3600
#minutes = duration // 60
#duration = duration % 60

#print(f'{days}:{hours}:{minutes}:{duration}')


#Ex.26

#from time import asctime

#now_time = asctime()
#print(now_time)


#Ex.27

#year = int(input("Enter a year: "))

#a = year % 19
#b = year // 100
#c = year % 400
#d = b // 4
#e = b % 4
#f = (b + 8) // 25
#g = (b - f + 1) // 3
#h = (19 * a + b - d - g + 15) % 30
#i = c // 4
#k = c % 4
#l = (32 + 2 * e + 2 * i - h - k) % 7
#m = (a + 11 * h + 22 * l) // 451
#month = (h + l - 7 * m +114) // 31
#day = 1 + ((h + l - 7 * m +114) % 31)

#print(f'The date of Easter: {month} month and {day} day in this year {year}')


#Ex.28

#height = int(input("Enter a height: "))
#weight = int(input("Enter a weight: "))

#BMI = weight / (height * height)
#print(f"Body mass index is {BMI}")

#Ex.29

#T = int(input("Enter a temperature: "))
#V = float(input("Enter a wind speed: "))

#WCI = 13.12 + 0.6215 * T - 11.37 * V ** 0.16 + 0.3965 * T * V ** 0.16

#print(f"The wind chill index is {int(WCI)}")

#Ex.30

#degrees = int(input("Enter a temperature in degrees: "))

#kelvin = degrees + 273.15
#farenheit = degrees * 9 / 5 + 32

#print(f'Temperature in Kelvin: {kelvin} \nFarenheit: {farenheit}')