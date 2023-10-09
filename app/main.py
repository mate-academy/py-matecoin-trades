import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    # Read the trades data from the JSON file
    with open(trades_file, "r") as f:
        trades = json.load(f)

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought:
            bought = Decimal(bought)
            earned_money -= bought * matecoin_price
            matecoin_account += bought

        if sold:
            sold = Decimal(sold)
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
