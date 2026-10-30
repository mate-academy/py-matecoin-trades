import json
from decimal import Decimal


def calculate_profit(trades_file_name: str) -> None:
    with open(trades_file_name, "r", encoding="utf-8") as trades_file:
        trades = json.load(trades_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(str(trade["matecoin_price"]))

        if trade.get("bought") is not None:
            bought = Decimal(str(trade["bought"]))
            matecoin_account += bought
            earned_money -= bought * price

        if trade.get("sold") is not None:
            sold = Decimal(str(trade["sold"]))
            matecoin_account -= sold
            earned_money += sold * price

    profit = {
        "earned_money": format(earned_money, "f"),
        "matecoin_account": format(matecoin_account, "f"),
    }

    with open("profit.json", "w", encoding="utf-8") as profit_file:
        json.dump(profit, profit_file, indent=2)
