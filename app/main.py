import json
from decimal import Decimal


def calculate_profit(trades_file : str) -> dict:
    with open(trades_file, "r", encoding="utf-8") as file:
        trades = json.load(file)

    total_profit = Decimal("0")
    matecoin_balance = Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"].replace(",", "."))
            price = Decimal(trade["matecoin_price"].replace(",", "."))
            matecoin_balance += bought
            total_profit -= bought * price
        if trade["sold"] is not None:
            sold = Decimal(trade["sold"].replace(",", "."))
            price = Decimal(trade["matecoin_price"].replace(",", "."))
            matecoin_balance -= sold
            total_profit += sold * price

    result = {
        "earned_money": str(total_profit),
        "matecoin_account": str(matecoin_balance)
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=2)
