import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as source_file:
        trades = json.load(source_file)

    earned_money = Decimal("0.0")
    mate_coin_account = Decimal("0.0")

    for trade in trades:
        mate_coin_price = Decimal(trade.get("matecoin_price"))
        if bought := trade.get("bought"):
            earned_money -= Decimal(bought) * mate_coin_price
            mate_coin_account += Decimal(bought)
        if sold := trade.get("sold"):
            earned_money += Decimal(sold) * mate_coin_price
            mate_coin_account -= Decimal(sold)

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(mate_coin_account)
    }

    with open("profit.json", "w") as destination_file:
        json.dump(profit, destination_file, indent=2)
