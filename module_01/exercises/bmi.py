print('Hello.')
print('I am BMI Calculator, what you want?')

weight = int(input('Tell me your weight [kg]: '))
height = int(input('Tell me your height [cm]: '))

bmi = int((weight) / ((height / 100) ** 2))

print(f'Your BMI is: {bmi}')

if bmi < 16:
    print('You are Severe Thinness')
elif 16 < bmi < 17:
    print('You are Moderate Thinness')
elif 17 < bmi < 18.5:
    print('You are Mild Thinness')
elif 18.5 < bmi < 25:
    print('You are Normal')
elif 25 < bmi < 30:
    print('You are Overweight')
elif 30 < bmi < 35:
    print('You are Obese Class I')
elif 35 < bmi < 40:
    print('You are Obese Class II')
elif bmi > 40:
    print('You are Obese Class III')
else:
    print('Something goes wrong!')