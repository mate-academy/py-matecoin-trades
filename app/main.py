import json
from decimal import Decimal
from pathlib import Path
from typing import List, Dict, Any


class Transaction:
    transactions: List["Transaction"] = []

    def __init__(
        self,
        bought: Decimal = Decimal(0),
        sold: Decimal = Decimal(0),
        price: Decimal = Decimal(0),
    ) -> None:
        self.bought = bought
        self.sold = sold
        self.price = price

    @property
    def cost(self) -> Decimal:
        return self.bought * self.price

    @property
    def revenue(self) -> Decimal:
        return self.sold * self.price

    @classmethod
    def total_cost(cls) -> Decimal:
        return sum(transaction.cost for transaction in cls.transactions)

    @classmethod
    def total_revenue(cls) -> Decimal:
        return sum(transaction.revenue for transaction in cls.transactions)

    @classmethod
    def total_matecoin_bought(cls) -> Decimal:
        return sum(transaction.bought for transaction in cls.transactions)

    @classmethod
    def total_matecoin_sold(cls) -> Decimal:
        return sum(transaction.sold for transaction in cls.transactions)


def calculate_profit(json_file: str) -> None:
    base_dir = Path(__file__).resolve().parent.parent
    trades_path = base_dir.joinpath("app", json_file)
    profit_path = base_dir.joinpath("profit.json")

    with open(trades_path, "r") as file:
        transactions_data: List[Dict[str, Any]] = json.load(file)

    transactions = [
        Transaction(
            Decimal(transaction_data.get("bought"))
            if transaction_data.get("bought") is not None
            else Decimal(0),
            Decimal(transaction_data.get("sold"))
            if transaction_data.get("sold") is not None
            else Decimal(0),
            Decimal(transaction_data["matecoin_price"]),
        )
        for transaction_data in transactions_data
    ]
    Transaction.transactions.extend(transactions)

    profit_amount = Transaction.total_revenue() - Transaction.total_cost()
    matecoin_amount = (
        Transaction.total_matecoin_bought() - Transaction.total_matecoin_sold()
    )

    output = {
        "earned_money": str(profit_amount),
        "matecoin_account": str(matecoin_amount),
    }

    with open(profit_path, "w") as file:
        json.dump(output, file, indent=2)

    Transaction.transactions = []
