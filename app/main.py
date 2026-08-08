import json
from decimal import Decimal


def calculate_profit(trades_information: str) -> None:
    with open(trades_information, "r") as trades_file:
        trades = json.load(trades_file)

    earned_money, matecoin_account = 0, 0

    for transaction in trades:

        if transaction.get("sold") is not None:
            earned_money += Decimal(transaction["sold"])\
                * Decimal(transaction["matecoin_price"])
            matecoin_account -= Decimal(transaction["sold"])

        if transaction.get("bought") is not None:
            earned_money -= Decimal(transaction["bought"])\
                * Decimal(transaction["matecoin_price"])
            matecoin_account += Decimal(transaction["bought"])

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit_data, profit_file, indent=2)
