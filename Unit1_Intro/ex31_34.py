#Ex.31

#pressure = int(input("Enter pressure in kPa: "))

#kpa_to_pounds = pressure * 0.145
#kpa_mille = pressure * 7.5
#kpa_atmosphere = pressure * 0.0098

#print(f'Pressure in: \n\t- {kpa_to_pounds} pounds per square inch'
#      f'\n\t- {kpa_mille} millimeters of mercury'
#      f'\n\t- {kpa_atmosphere} atmosphere')


#Ex.32

#number = int(input("Enter a 4 digit number: "))

#s_number = str(number)
#sum = int(s_number[0]) + int(s_number[1]) + int(s_number[2]) + int(s_number[3])

#print(f'Sum of digits: {sum}')

#Ex.33

#num1 = int(input('Enter the first number: '))
#num2 = int(input('Enter the second number: '))
#num3 = int(input('Enter the third number: '))

#min_num = min(num1, num2, num3)
#max_num = max(num1, num2, num3)
#mid_num = (num1 + num2 + num3) - min_num - max_num

#print(f'The minimum number is: {min_num}')
#print(f'The maximum number is: {max_num}')
#print(f'The middle number is: {mid_num}')


#Ex.34

#count_loaves = int(input("Enter a number of loaves: "))

#discount_rate = 0.6
#l_price = 3.49

#without_discount = count_loaves * l_price
#discount_price = without_discount * discount_rate
#total_price = without_discount - discount_price

#print(f'Your bought {count_loaves} loaves of bread:'
#      f'\n\t - {without_discount:.2f} dollars'
#      f'\n\t - {discount_price:.2f} dollars discount'
#      f'\n\t - {total_price:.2f} dollars in total')