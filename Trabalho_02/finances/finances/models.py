from datetime import datetime
from typing import List, Optional

class Transaction:
    def __init__(self, amount: float, category: int, description: str = "") -> None:
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now()

    def __str__(self) -> str:
        return f"Transação: {self.description}, R$ {self.amount:.2f} ({self.category})"

    def update(self, **attributes) -> None:
        for key, value in attributes.items():
            setattr(self, key, value)

class Account:
    def __init__(self, name: str) -> None:
        self.name = name
        self.balance = 0.0
        self.transactions: List[Transaction] = []
        self.client = None

    def add_transaction(self, amount: float, category: int, description: str = "") -> Transaction:
        transaction = Transaction(amount, category, description)
        self.transactions.append(transaction)
        self.balance -= amount
        return transaction

    def get_transactions(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, category: Optional[int] = None) -> List[Transaction]:
        filtered_transactions = self.transactions

        if start_date:
            filtered_transactions = [t for t in filtered_transactions if t.date >= start_date]
        if end_date:
            filtered_transactions = [t for t in filtered_transactions if t.date <= end_date]
        if category is not None:
            filtered_transactions = [t for t in filtered_transactions if t.category == category]

        return filtered_transactions

class Investment:
    def __init__(self, tipo: int, amount: float, rate_of_return: float) -> None:
        self.type = tipo
        self.initial_amount = amount
        self.date_purchased = datetime.now()
        self.rate_of_return = rate_of_return
        self.client = None

    def calculate_value(self) -> float:
        months = (datetime.now() - self.date_purchased).days // 30
        return self.initial_amount * (1 + self.rate_of_return) ** months

    def sell(self, account: Account) -> None:
        current_value = self.calculate_value()
        account.balance += current_value
        self.client.investments.remove(self)

class Client:
    def __init__(self, name: str) -> None:
        self.name = name
        self.accounts: List[Account] = []
        self.investments: List[Investment] = []

    def add_account(self, account_name: str) -> Account:
        account = Account(account_name)
        account.client = self
        self.accounts.append(account)
        return account

    def add_investment(self, investment: Investment) -> None:
        investment.client = self
        self.investments.append(investment)

    def get_net_worth(self) -> float:
        account_balance = sum(account.balance for account in self.accounts)
        investment_value = sum(investment.calculate_value() for investment in self.investments)
        return account_balance + investment_value
    
from datetime import datetime
from typing import List, Optional

class Investment:
    def __init__(self, tipo: int, amount: float, rate_of_return: float) -> None:
        """Inicia um objeto da classe Investment
        Args:
            tipo(int): Tipo do investimento
            amount(float): Valor do investimento
            rate_of_return(float): Taxa de retorno do investimento
        """
        self.type = tipo
        self.amount = amount
        self.date_purchased = datetime.now()
        self.rate_of_return = rate_of_return
        self.client = None

    def calculate_value(self) -> float:
        """Calcula o valor atual do investimento"""
        months = (datetime.now() - self.date_purchased).days // 30
        return self.amount * (1 + self.rate_of_return) ** months

    def sell(self, account: Account) -> None:
        """Vende o investimento
        Args:
            account(Account): Conta que está vendendo o investimento
        """
        account.balance += self.calculate_value()
        self.client.investments.remove(self)

class Client:
    def __init__(self, name: str) -> None:
        """Inicia um objeto da classe Client
        Args:
            name(str): Nome do cliente
        """
        self.name = name
        self.accounts: List[Account] = []
        self.investments: List[Investment] = []

    def add_account(self, account_name: str) -> Account:
        """Cria uma conta para o cliente
        Args:
            account_name(str): Nome da conta criada
        Returns:
            Account: Conta criada
        """
        account = Account(account_name)
        account.client = self
        self.accounts.append(account)
        return account

    def add_investment(self, investment: Investment) -> None:
        """Adiciona um investimento ao cliente
        Args:
            investment(Investment): Investimento adicionado
        """
        investment.client = self
        self.investments.append(investment)

    def get_net_worth(self) -> float:
        """Calcula a soma do valor das contas e investimentos do cliente
        Returns:
            float: soma dos valores das contas e investimentos
        """
        account_balance = sum(account.balance for account in self.accounts)
        investment_value = sum(investment.calculate_value() for investment in self.investments)
        return account_balance + investment_value