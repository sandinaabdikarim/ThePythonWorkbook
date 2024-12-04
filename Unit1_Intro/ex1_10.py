#Ex. 1

#print('my name is Sandina')
#print('My address: Varlamova 27 street, Almaty city, Kazakhstan')


#Ex.2

#name = input('What is your name? ')
#print(f'Hello {name}!')

#Ex.3

#width = float(input("Enter a width of the room: "))
#length = float(input("Enter a length of the room: "))

#print(f"Your area of the room: {width * length}")

#Ex.4

#length_field = float(input("Enter a length in feet: "))
#width_field = float(input("Enter a width in feet: "))

#acre = 43560

#print(f'Your field are in acres: {(length_field * width_field) / acre}')


#Ex.5

#con_less_1l = 0.10
#con_more_1l = 0.25

#num_cont_less = int(input("Enter number of containers which less 1 liter: "))
#num_cont_more = int(input("Enter number of containers which more 1 liter: "))

#deposit = (num_cont_less * con_less_1l) + (num_cont_more * con_more_1l)
#print(f"Your total deposit is {deposit:.2f} dollars")

#Ex.6

#coast_meal = int(input("Enter a coast meal: "))

#tax_amount = 12
#tax_tip = 18

#coast_tax_tip = coast_meal * tax_tip / 100
#coast_tax_amount = coast_meal * tax_amount / 100
#grand_total = coast_meal + coast_tax_amount + coast_tax_tip

#print(f'Your grand total is {grand_total:.2f}')
#print(f'\t Including tax amount: {coast_tax_amount:.2f}')
#print(f'\t Including tax tip: {coast_tax_tip:.2f}')


#Ex.7

#positive_integer = int(input("Enter a positive integer: "))
#sum_positive_integer = positive_integer * (positive_integer + 1) / 2
#print(sum_positive_integer)

#Ex.8

#widgets_weigh = 75
#gizmo_weigh = 112

#widgets = int(input("How many widgets do you want?: "))
#gizmos = int(input("How many gizmos do you want?: "))

#total = widgets * widgets_weigh + gizmos * gizmo_weigh
#print(f'Total weigh: {total}')

#Ex.9

#percent_interest = 4

#amount_deposit = float(input("Enter the amount deposit: "))

#amount_deposit_1y = amount_deposit + (amount_deposit * percent_interest / 100)
#amount_deposit_2y = amount_deposit_1y + (amount_deposit_1y * percent_interest / 100)
#amount_deposit_3y = amount_deposit_2y + (amount_deposit_2y * percent_interest / 100)

#print(f"Your amount of deposit after 1 year is {amount_deposit_1y:.2f}")
#print(f"Your amount of deposit after 2 years is {amount_deposit_2y:.2f}")
#print(f"Your amount of deposit after 3 years is {amount_deposit_3y:.2f}")

#Ex.10
#import math

#int_a = int(input("Enter an integer a: "))
#int_b = int(input("Enter an integer b: "))

#print(int_a + int_b)
#print(int_b - int_a)
#print(int_a * int_b)
#print(int_a / int_b)
#print(int_a % int_b)
#print(math.log10(int_a))
#print(int_a ** int_b)


