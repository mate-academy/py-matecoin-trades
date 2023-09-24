import json
from decimal import Decimal


def calculate_profit(input_file: str) -> None:
    with open(input_file, "r") as f:
        trades_data = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade["matecoin_price"])
        if bought is not None:
            bought = Decimal(bought)
            earned_money -= bought * matecoin_price
            matecoin_account += bought
        if sold is not None:
            sold = Decimal(sold)
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    result_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as outfile:
        json.dump(result_data, outfile, indent=2)
