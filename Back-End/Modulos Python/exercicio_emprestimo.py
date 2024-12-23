from datetime import datetime
from dateutil.relativedelta import relativedelta


valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos


data_parcelas = []
data_parcela = data_emprestimo

while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela = data_parcela + relativedelta(months=1)


numero_parcelas = len(data_parcelas)

valor_parcela = valor_total / numero_parcelas

vezes = 1

saldo_devedor = valor_total - valor_parcela
for data in data_parcelas:
    print(f"{vezes}x {data.strftime('%d/%m/%Y')} - R$ {valor_parcela:,.2f}"
          f" (Seu saldo devedor é R${saldo_devedor:,.2f})"
          )
    saldo_devedor -= valor_parcela
    vezes += 1

print()
print(f'Você pegou R${valor_total:,.2f} para pagar'
      f'em {delta_anos.years} anos'
      f'({numero_parcelas} meses) em parcelas de '
      f'R${valor_parcela:,.2f} cada.'
      )
