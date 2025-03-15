from datetime import datetime, timedelta
from pytz import timezone
from dateutil.relativedelta import relativedelta

data_str_data = '2024-01-20 07:11:23'
data = datetime.strptime(data_str_data, '%Y-%m-%d %H:%M:%S')
# print(data)

data_str_br = '21/02/2024 '
data_br = datetime.strptime(data_str_br, '%d/%m/%Y ')
# print(data_br)

data2 = datetime(2024, 1, 20, 7)
# print(data2)

data3 = datetime.now(tz=timezone('Asia/Tokyo'))
# print(data3)
# print(data.timestamp())
# print(datetime.fromtimestamp(data.timestamp()))

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/01/2024 07:11:23', fmt)
data_fim = datetime.strptime('19/08/2024 07:11:23', fmt)

delta = timedelta(days=10, hours=2)
delta = relativedelta(data_fim, data_inicio)
print(delta)
print(data_inicio + delta)
print(data_inicio - relativedelta(days=10))  # Para criar uma data

print(data_inicio.strftime(fmt))  # Para convertar a hora em hora pt-br
