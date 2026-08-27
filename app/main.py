import json
from decimal import Decimal


def calculate_profit(
        trades_json_file: str,
        profit_file_path: str = "profit.json"
) -> None:
    with open(trades_json_file, "r") as trades_file:
        trades_data = json.load(trades_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            earned_money -= bought * price
            matecoin_account += bought

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            earned_money += sold * price
            matecoin_account -= sold

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open(profit_file_path, "w") as profit_file:
        json.dump(profit_data, profit_file, indent=2)
