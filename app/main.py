import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    try:
        with open(trades_file, "r") as file:
            trades = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        trades = []

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought_volume = Decimal(trade["bought"])
            matecoin_account += bought_volume
            earned_money -= bought_volume * matecoin_price
        if trade["sold"]:
            sold_volume = Decimal(trade["sold"])
            matecoin_account -= sold_volume
            earned_money += sold_volume * matecoin_price

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
