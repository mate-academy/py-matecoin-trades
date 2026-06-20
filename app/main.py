import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades) as file:
        transactions = json.load(file)

        bought_coins = 0
        sold_coins = 0
        income = 0
        expenses = 0
        profit_string = {}

        for transaction in transactions:
            price = Decimal(transaction["matecoin_price"])
            if not transaction["bought"] is None:
                bought = Decimal(transaction["bought"])
                bought_coins += bought
                expenses += (bought * price)

            if not transaction["sold"] is None:
                sold = Decimal(transaction["sold"])
                sold_coins += sold
                income += (sold * price)

        profit_string["earned_money"] = str(income - expenses)
        profit_string["matecoin_account"] = str(bought_coins - sold_coins)

    with open("profit.json", "w") as file:
        json.dump(profit_string, file, indent=2)
