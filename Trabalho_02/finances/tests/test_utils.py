import pytest
from datetime import datetime, timedelta
from finances.models import Client, Account, Investment
from finances.utils import generate_report, future_value_report

@pytest.fixture
def sample_client():
    client = Client("Test Client")
    account = client.add_account("Test Account")
    account.add_transaction(1000.0, 1, "Deposit")
    account.add_transaction(-200.0, 2, "Withdrawal")
    investment = Investment(1, 5000.0, 0.05)
    client.add_investment(investment)
    return client

def test_generate_report(sample_client):
    report = generate_report(sample_client)
    assert "Nome: Test Client" in report
    assert "Contas: Test Account" in report
    assert "Investimentos: 1" in report
    assert "Valor Total: R$" in report

def test_future_value_report(sample_client):
    future_date = datetime.now() + timedelta(days=365)
    report = future_value_report(sample_client, future_date)
    assert "Projeção de Rendimentos - Test Client" in report
    assert "Data da Projeção:" in report
    assert "Investimento Tipo 1:" in report
    assert "Valor Atual: R$" in report
    assert "Valor Projetado: R$" in report
    assert "Rendimento: R$" in report