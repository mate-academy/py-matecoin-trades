from decimal import Decimal
import json


def calculate_profit(name: str) -> None:
    profit = Decimal(0)
    coins = Decimal(0)

    with open(name, "r") as f:
        transactions = json.load(f)
        for transaction in transactions:
            if transaction["bought"]:
                profit -= (
                    Decimal(transaction["bought"])
                    * Decimal(transaction["matecoin_price"])
                )
                coins += Decimal(transaction["bought"])
            if transaction["sold"]:
                profit += (
                    Decimal(transaction["sold"])
                    * Decimal(transaction["matecoin_price"])
                )
                coins -= Decimal(transaction["sold"])
    with open("profit.json", "w") as f:
        dict_result = {"earned_money": str(profit),
                       "matecoin_account": str(coins)}
        json.dump(dict_result, f, indent=2)
