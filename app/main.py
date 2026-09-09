import json
from decimal import Decimal


def calculate_profit(trades_file_path: str) -> None:
    with open(trades_file_path, "r", encoding="utf-8") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade.get("bought") is not None:
            bought = Decimal(trade["bought"])
            earned_money -= bought * price
            matecoin_account += bought

        if trade.get("sold") is not None:
            sold = Decimal(trade["sold"])
            earned_money += sold * price
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
