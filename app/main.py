import json
from decimal import Decimal


def calculate_profit(trades_file_name: str) -> None:
    with open(trades_file_name, "r", encoding="utf-8") as source_file:
        trades = json.load(source_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_amount = Decimal(trade["bought"])
            earned_money -= bought_amount * price
            matecoin_account += bought_amount

        if trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            earned_money += sold_amount * price
            matecoin_account -= sold_amount

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as destination_file:
        json.dump(profit_data, destination_file, indent=2)
