import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    saldo = 0
    matecoin_account = 0
    with (open(file_name, "r") as trades,
          open("profit.json", "w") as profit):
        transactions = json.load(trades)
        for transaction in transactions:
            coin_price = Decimal(transaction["matecoin_price"])
            if transaction["bought"]:
                bought = Decimal(transaction["bought"])
                matecoin_account += bought
                saldo -= bought * coin_price
            if transaction["sold"]:
                sold = Decimal(transaction["sold"])
                matecoin_account -= sold
                saldo += sold * coin_price
        profit_dict = {"earned_money": str(saldo),
                       "matecoin_account": str(matecoin_account)}
        json.dump(profit_dict, profit, indent=2)
