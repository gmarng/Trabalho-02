from finances import Client, Account, Investment, generate_report, future_value_report
from datetime import datetime, timedelta

client = Client("João Silva")

account = client.add_account("Conta Corrente")

account.add_transaction(1000, 1, "Salário")
account.add_transaction(-50, 2, "Compras no supermercado")

investment = Investment(1, 5000, 0.01)
client.add_investment(investment)

print("Relatório Atual:")
print(generate_report(client))

future_date = datetime.now() + timedelta(days=365)
print("\nRelatório de Projeção Futura:")
print(future_value_report(client, future_date))