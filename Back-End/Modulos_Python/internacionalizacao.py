import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')

print(calendar.calendar(2020))
print(locale.getlocale())
