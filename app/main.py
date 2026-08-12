import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as trades_file:
        trade_data = json.load(trades_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trade_data:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * price
        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file, indent=2)
