import json
from decimal import Decimal


def calculate_profit(file: str) -> None:
    with open(file, "r") as file_out:
        trades_data = json.load(file_out)
    money_profit = 0
    coin_account = 0

    for transaction in trades_data:
        if transaction["bought"]:
            money_profit -= Decimal(transaction["bought"])\
                * Decimal(transaction["matecoin_price"])
            coin_account += Decimal(transaction["bought"])
        if transaction["sold"]:
            money_profit += Decimal(transaction["sold"])\
                * Decimal(transaction["matecoin_price"])
            coin_account -= Decimal(transaction["sold"])

    data = {"earned_money": str(money_profit),
            "matecoin_account": str(coin_account)}

    with open("profit.json", "w") as file_in:
        json.dump(data, file_in, indent=2)

    return None
