import json
import os.path
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    full_path_name = os.path.join(os.path.dirname(__file__), trades_file)

    with open(full_path_name) as source_file:
        data_trades = json.load(source_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in data_trades:
        bought = (
            Decimal(trade["bought"])
            if trade["bought"] is not None else Decimal("0")
        )
        sold = (
            Decimal(trade["sold"])
            if trade["sold"] is not None else Decimal("0")
        )
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought > 0:
            earned_money -= bought * matecoin_price
            matecoin_account += bought
        if sold > 0:
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    base_dir = os.path.join(os.path.dirname(__file__), "..")
    full_path_result_file = (
        os.path.join(os.path.abspath(base_dir), "profit.json")
    )

    with open(full_path_result_file, "w") as json_file2:
        json.dump(profit_data, json_file2, indent=4)


calculate_profit("trades.json")
