import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(file_name, "r") as trades_file:
        trades: list[dict[str, str | None]] = json.load(trades_file)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade.get("bought"):
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * price

        if trade.get("sold"):
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * price

    profit_data: dict[str, str] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit_data, profit_file, indent=2)
