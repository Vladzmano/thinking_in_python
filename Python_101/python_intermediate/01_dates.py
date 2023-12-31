### Dates - Fechas ### formato posix

from datetime import datetime

now = datetime.now()

def print_date(date):
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(date.timestamp())
print_date(now)

timestamp = now.timestamp()

print (timestamp)

year_2023 = datetime(2023 ,7 ,6) # es obligatorio pasar datos obligatorios DD/MM/AA


print(year_2023)


from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today() # imprime la fecha del momento

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2023, 10, 6) # imprime la fecha definda

print(current_date.year)
print(current_date.month)
print(current_date.day)


## Operaciones confechas ##

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date # cuendo intentamos acceder a date o fecha todo bien, pero time no es accesible.
print(diff)

print(year_2023.time())

### time delta ## nos vale para operar con datos de fecha -franjas de fechas- Valores absolutos.

from datetime import timedelta

star_time_delta = timedelta(200, 100, 100, weeks = 10)
end_time_delta = timedelta(300, 100, 100, weeks = 13)

print(end_time_delta - star_time_delta)
print(end_time_delta + star_time_delta)
#print(end_time_delta * star_time_delta) no es posible