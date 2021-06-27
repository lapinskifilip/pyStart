nominal = 2500

seniority = int(input('Podaj staz pracy w latach: '))
sold = int(input('Ile sztuk towaru sprzedales: '))
worktime = int(input('Ile godzin przepracowales: '))

seniority_bonus = 0.1 if seniority > 2 else 0.02 * seniority
sold_bonus = 0.25 if sold > 30 else 0
worktime_bonus = 0.08 if worktime > 160 and seniority_bonus > 1 else 0.02

salary = nominal + (seniority_bonus * nominal) + (sold_bonus * nominal) + (worktime_bonus * nominal)

print(f'Zarobiles {salary}')

