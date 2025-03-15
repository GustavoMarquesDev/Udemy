import calendar

# print(calendar.calendar(2020))
# print(calendar.month(2020, 12))
# print(calendar.monthrange(2020, 12))
# print(list(enumerate(calendar.day_name)))
numero_primeiro_dia, ultimo_dia = calendar.monthrange(2020, 12)
print(calendar.day_name[numero_primeiro_dia])
print(calendar.day_name[calendar.weekday(2020, 12, ultimo_dia)])

for week in calendar.monthcalendar(2020, 12):
    print(list(enumerate(week)))
