from datetime import datetime
from typing import List
from .models import Client, Account, Investment

def generate_report(client: Client) -> str:
    """
    Gera um relatório financeiro para um cliente.

    Args:
        client (Client): O cliente para o qual o relatório será gerado.

    Returns:
        str: Uma string contendo o relatório financeiro formatado.
    """
    report: str = f"Relatório Financeiro - {client.name}\n"
    report += f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n"

    report += "Contas:\n"
    for account in client.accounts:
        report += f"- {account.name}: R$ {account.balance:.2f}\n"

    report += "\nInvestimentos:\n"
    for investment in client.investments:
        report += f"- Tipo {investment.type}: R$ {investment.calculate_value():.2f}\n"

    report += f"\nPatrimônio Líquido: R$ {client.get_net_worth():.2f}"

    return report

def future_value_report(client: Client, date: datetime) -> str:
    """
    Gera um relatório de projeção de rendimentos futuros para um cliente.

    Args:
        client (Client): O cliente para o qual o relatório será gerado.
        date (datetime): A data futura para a qual a projeção será calculada.

    Returns:
        str: Uma string contendo o relatório de projeção formatado.
    """
    months: int = (date - datetime.now()).days // 30
    
    report: str = f"Projeção de Rendimentos - {client.name}\n"
    report += f"Data da Projeção: {date.strftime('%d/%m/%Y')}\n\n"

    for investment in client.investments:
        future_value: float = investment.initial_amount * (1 + investment.rate_of_return) ** months
        report += f"Investimento Tipo {investment.type}:\n"
        report += f"  Valor Inicial: R$ {investment.initial_amount:.2f}\n"
        report += f"  Valor Projetado: R$ {future_value:.2f}\n"
        report += f"  Rendimento: R$ {future_value - investment.initial_amount:.2f}\n\n"

    return report

def generate_report(client: Client) -> str:
    """Cria um relatório para o cliente
    Args:
        client(Client): Cliente sobre o qual será o relatório
    Returns:
        str: Relatório sobre o cliente
    """
    valor = client.get_net_worth()
    report = f"Nome: {client.name}\n"
    report += f"Contas: {', '.join([account.name for account in client.accounts])}\n"
    report += f"Investimentos: {len(client.investments)}\n"
    report += f"Valor Total: R$ {valor:.2f}"
    return report

def future_value_report(client: Client, date: datetime) -> str:
    """Gera um relatório de projeção de rendimentos futuros para um cliente
    Args:
        client(Client): Cliente para o qual será gerado o relatório
        date(datetime): Data futura para a projeção
    Returns:
        str: Relatório de projeção de rendimentos
    """
    months = (date - datetime.now()).days // 30
    
    report = f"Projeção de Rendimentos - {client.name}\n"
    report += f"Data da Projeção: {date.strftime('%d/%m/%Y')}\n\n"

    for investment in client.investments:
        future_value = investment.amount * (1 + investment.rate_of_return) ** months
        report += f"Investimento Tipo {investment.type}:\n"
        report += f"  Valor Atual: R$ {investment.calculate_value():.2f}\n"
        report += f"  Valor Projetado: R$ {future_value:.2f}\n"
        report += f"  Rendimento: R$ {future_value - investment.calculate_value():.2f}\n\n"

    return report