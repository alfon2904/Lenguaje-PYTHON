# Trabajando con fechas y horas en Python

from datetime import datetime, timedelta
import locale

# 1. Obtener la fecha y hora actual
#now = datetime.now()
#print(f"Fecha y hora actual: {now}")
"""
# 2. Crear una fecha y hora específica
specific_date = datetime(2025, 10, 11, 15, 30, 0)
print(f"Fecha y hora específica: {specific_date}")

format_date = specific_date.strftime("%A %B %Y %H:%M:%S")
print(f"Fecha formateada: {format_date}")

# 3. Formatear fechas
# método strftime() para formatear fechas
# pasarle el objeto datetime y el formato especificado
# formato:
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

#-------Example of section 2 and 3 combined-------#
specific_date = datetime(2025, 10, 11, 15, 30, 0)
print(f"Fecha y hora específica: {specific_date}")
#FULL NAME OF DAY, FULL NAME OF MONTH, YEAR, HOUR:MINUTE:SECOND
format_date = specific_date.strftime("%A %B %Y %H:%M:%S")
print(f"Fecha formateada larga: {format_date}\n")
#Abbreviated name.
format_date = specific_date.strftime("%a %b %y %H:%M:%S")
print(f"Fecha formateada corta: {format_date}\n")
#With only numbers.
format_date = specific_date.strftime("%d/%m/%y/ - %H:%M:%S")
print(f"Fecha formateada numerica: {format_date}\n")
#Change order of date.
format_date = specific_date.strftime("%Y - %m - %d - %H:%M:%S")
print(f"Fecha formateada numerica otro orden YYYY-MM-DD: {format_date}\n")
#Without time.
format_date = specific_date.strftime("%d - %m - %Y")
print(f"Fecha formateada numerica sin tiempo y DD-MM-YYYY: {format_date}\n")
#-------End of example-------#


# 4. Operaciones con fechas (sumar/restar dias, minutos, horas, meses)
now = datetime.now()
print(f"Fecha y hora actual: {now}\n")

yesterday = datetime.now() - timedelta(days=1)
print(f"Ayer: {yesterday}\n")

tomorrow = datetime.now() + timedelta(days=1)
print(f"Mañana: {tomorrow}\n")

one_hour_after = datetime.now() + timedelta(hours=1)
print(f"Una hora después: {one_hour_after} \n")

next_week = datetime.now() + timedelta(weeks=1)
print(f"La próxima semana: {next_week}\n")

next_month = datetime.now() + timedelta(days=30)
print(f"El próximo mes (aproximado): {next_month}\n")

# 5. Obtener componentes individuales de una fecha
now = datetime.now()
format_date = now.strftime("%d/%m/%Y - %H:%M:%S")
print(f"Fecha y hora actual: {format_date}\n")

# Obtener año, mes y día
year = now.year
print(f"Año: {year}")
month = now.month
print(f"Mes: {month}")
day = now.day
print(f"Día: {day}")
"""
# 6. Calcular la diferencia entre 2 fechas
#date1 = datetime.now()
#date2 = datetime(2025, 2, 12, 15, 30, 0)
#difference = date2 - date1
#print(f"Diferencia entre las fechas: {difference}\n")
#-------------------------------------------
#calcular edad restando fecha de nacimiento a la fecha actual
now = datetime.now()
birth_date = datetime(2004, 11, 29)
age = now.year - birth_date.year
if (now.month, now.day) < (birth_date.month, birth_date.day):
    age -= 1
print(f"Edad: {age} años")





