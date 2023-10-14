import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades_data = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        if trade.get("bought") is not None:
            bought_amount = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money -= bought_amount * matecoin_price
            matecoin_account += bought_amount
        if trade.get("sold") is not None:
            sold_amount = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money += sold_amount * matecoin_price
            matecoin_account -= sold_amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "a") as file:
        json.dump(result, file, indent=2)
# mdm