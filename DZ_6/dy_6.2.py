initial_number = int(input('Введіть число від 0 до 8640000: '))

seconds_in_minut, seconds = divmod(initial_number, 60)
minut_in_hour, minutes = divmod(seconds_in_minut, 60)
days, hours = divmod(minut_in_hour, 24)

name_of_days = days % 10

if name_of_days == 1 and days != 11:
    day_word = 'день'
elif 2 <= name_of_days <= 4 and not 12 <= days <= 14:
    day_word = 'дні'
else:
    day_word = 'днів'

hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)

result = f'{days} {day_word}, {hours}:{minutes}:{seconds}'
print(result)


#0 -> 0 днів, 00:00:00
#224930 -> 2 дні, 14:28:50
#466289 -> 5 днів, 09:31:29
#950400 -> 11 днів, 00:00:00
#1209600 -> 14 днів, 00:00:00
#1900800 - > 22 дні, 00:00:00
#8639999 -> 99 днів, 23:59:59
#22493 -> 0 днів, 06:14:53
#7948799 -> 91 день, 23:59:59
