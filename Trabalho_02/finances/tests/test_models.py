import pytest
from datetime import datetime, timedelta
from finances.models import Transaction, Account, Investment, Client

def test_transaction_init():
    t = Transaction(100.0, 1, "Test transaction")
    assert t.amount == 100.0
    assert t.category == 1
    assert t.description == "Test transaction"
    assert isinstance(t.date, datetime)

def test_transaction_str():
    t = Transaction(100.0, 1, "Test transaction")
    assert str(t) == "Transação: Test transaction, R$ 100.00 (1)"

def test_transaction_update():
    t = Transaction(100.0, 1, "Test transaction")
    t.update(amount=200.0, category=2, description="Updated transaction")
    assert t.amount == 200.0
    assert t.category == 2
    assert t.description == "Updated transaction"

def test_account_init():
    a = Account("Test Account")
    assert a.name == "Test Account"
    assert a.balance == 0.0
    assert len(a.transactions) == 0

def test_account_add_transaction():
    a = Account("Test Account")
    t = a.add_transaction(100.0, 1, "Test transaction")
    assert len(a.transactions) == 1
    assert a.balance == -100.0
    assert isinstance(t, Transaction)

def test_account_get_transactions():
    a = Account("Test Account")
    a.add_transaction(100.0, 1, "Transaction 1")
    a.add_transaction(200.0, 2, "Transaction 2")
    a.add_transaction(300.0, 1, "Transaction 3")

    assert len(a.get_transactions()) == 3
    assert len(a.get_transactions(category=1)) == 2
    assert len(a.get_transactions(start_date=datetime.now() - timedelta(days=1))) == 3
    assert len(a.get_transactions(end_date=datetime.now() + timedelta(days=1))) == 3

def test_investment_init():
    i = Investment(1, 1000.0, 0.05)
    assert i.type == 1
    assert i.amount == 1000.0
    assert i.rate_of_return == 0.05
    assert isinstance(i.date_purchased, datetime)

def test_investment_calculate_value():
    i = Investment(1, 1000.0, 0.05)
    i.date_purchased = datetime.now() - timedelta(days=30)
    assert i.calculate_value() == pytest.approx(1050.0)

def test_investment_sell():
    c = Client("Test Client")
    a = c.add_account("Test Account")
    i = Investment(1, 1000.0, 0.05)
    c.add_investment(i)

    i.sell(a)
    assert a.balance == pytest.approx(1000.0)
    assert len(c.investments) == 0

def test_client_init():
    c = Client("Test Client")
    assert c.name