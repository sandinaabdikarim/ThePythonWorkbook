#Ex.11

#value_user = float(input("Enter the miles per gallon for the user: "))

#miles = 1.609
#gallons = 3.785

#l_per_km = (gallons / miles * 100) / value_user
#print(f"The equivalent fuel efficiency in Canadians units: {l_per_km:.2f} l/100km")


#Ex.12

#from math import radians, sin, cos, acos

#t1 = radians(float(input("Enter a latitude of the first point in degrees Celsius: ")))
#g1 = radians(float(input("Enter a longitude of the first point in degrees Celsius: ")))
#t2 = radians(float(input("Enter a latitude of the second point in degrees Celsius: ")))
#g2 = radians(float(input("Enter a longitude of the second point in degrees Celsius: ")))

#ave_radius = 6371.01

#distance = ave_radius * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))

#print(f'Distance between two points: {distance:.2f}km')


#Ex.13

#penny = 1
#nickel = 5
#dime = 10
#quarter = 25
#loonie = 100
#toonie = 200

#num_cents = int(input("How many cents do yo want to change?: "))

#d_toonies = num_cents // toonie
#num_cents = num_cents % toonie
#d_loonies = num_cents // loonie
#num_cents = num_cents % loonie
#d_quarters = num_cents // quarter
#num_cents = num_cents % quarter
#d_dimes = num_cents // dime
#num_cents = num_cents % dime
#d_nickels = num_cents // nickel
#num_cents = num_cents % nickel
#d_pennies = num_cents // penny
#num_cents = num_cents % penny

#print(f'Your change: \n\t- {d_toonies} toonies,'
#      f'\n\t- {d_loonies} loonies, \n\t- {d_quarters} quarters,'
#      f'\n\t- {d_dimes} dimes, \n\t- {d_nickels} nickels,'
#      f'\n\t- {d_pennies} pennies')


#Ex.14

#one_foot_inch = 12
#one_inch_cm = 2.54

#foot = int(input("Write number of feet: "))
#inches = int(input("Write number of inches: "))

#total = (foot * one_inch_cm * one_foot_inch + inches * one_inch_cm) * 2.54
#print(f'Your height: {total:.2f} cm')

#Ex.15

#foot_inch = 12
#mile_foot = 5280
#yard_foot = 3

#feet = int(input("Number of feet: "))

#print(f'{feet} feet = {foot_inch * feet:.2f} inches')
#print(f'{feet} feet = {feet / yard_foot:.2f} yards')
#print(f'{feet} feet = {feet / mile_foot:.2f} miles')


#Ex.16
#from math import pi

#r = int(input('Write a number of radius: '))

#area = pi * r ** 2
#volume = 4/3 * pi * r ** 3

#print(f'The area of the circle is {area:.2f}')
#print(f'The volume of the sphere is {volume:.2f}')

#Ex.17

#heat_capacity = 4.186
#elect_price = 8.9
#j_to_kwh = 2.777 * 10 ** (-7)
#mass = float(input("Enter the mass of the water: "))
#temperature = float(input("Enter the temperature: "))

#q = mass * temperature * heat_capacity
#kwh = q * j_to_kwh
#cost = kwh * elect_price

#print(f'Total amount of energy: {q} joules')
#print(f'That much energy will cost {cost:.2f}')

#Ex.18

#import math
#radius = int(input("Enter a radius: "))
#height = int(input("Enter a height: "))

#area = math.pi * radius ** 2
#volume = area * height

#print(f"The volume of the area is {volume:.1f}")


#Ex.19
#import math
#acceleration = 9.8
#initial_speed = 0

#height = int(input("Enter a height in meters: "))

#final_speed = math.sqrt(initial_speed ** 2 + 2 * acceleration * height)
#print(f"The final speed is {final_speed} m/s")

#Ex.20

#R = 8.314

#P = int(input("Enter a pressure in Pascals: "))
#V = int(input("Enter a volume in liters: "))
#T = int(input("Enter temperature in degrees: "))

#deg_to_kelvin = T + 273.15
#n = P * V / (R * T)

#print(f'Amount of gas in moles: {n:.2f}')
