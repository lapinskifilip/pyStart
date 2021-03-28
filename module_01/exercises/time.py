import datetime

wake_up_seconds = int(input('Podaj czas pobudki w sekundach: '))
lunch_seconds = int(input('Podaj czas lunchu w sekundach: '))
sleep_time_seconds = int(input('Podaj czas do spania w sekundach: '))

wake_up = str(datetime.timedelta(seconds=wake_up_seconds))
lunch = str(datetime.timedelta(seconds=lunch_seconds))
sleep_time = str(datetime.timedelta(seconds=sleep_time_seconds))

print(f'Pobudka jest o {wake_up}')
print(f'Lunch jest o {lunch}')
print(f'Czas do spania jest o {sleep_time}')