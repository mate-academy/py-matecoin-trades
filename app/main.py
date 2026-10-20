import json
from decimal import Decimal


def calculate_profit(trades_file: str = "trades.json") -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    matecoin_account = Decimal("0.0")
    earned_money = Decimal("0.0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade.get("sold") is not None:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += price * sold

        if trade.get("bought") is not None:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= price * bought

    new_json_file = {"earned_money": str(earned_money),
                     "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as file:
        json.dump(new_json_file, file, indent=2)
