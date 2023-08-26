import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as trades_file:
        trades = json.load(trades_file)

    profit = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    for trade in trades:
        price = Decimal(trade.get("matecoin_price"))
        if bougth := trade.get("bought"):
            profit["earned_money"] -= Decimal(bougth) * price
            profit["matecoin_account"] += Decimal(bougth)
        if sold := trade.get("sold"):
            profit["earned_money"] += Decimal(sold) * price
            profit["matecoin_account"] -= Decimal(sold)

    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])

    with open("profit.json", "w") as output_file:
        json.dump(profit, output_file, indent=2)
