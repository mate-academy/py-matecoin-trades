import json
from decimal import Decimal
import os


def calculate_profit(file_name: str) -> None:
    file_path = os.path.join("app", file_name)
    with open(file_path, "r") as file:
        trades = json.load(file)

    profit = Decimal("0.00")
    current_coin_account = Decimal("0.00")

    for trade_item in trades:
        if trade_item["bought"]:
            profit -= Decimal(trade_item["bought"])\
                * Decimal(trade_item["matecoin_price"])
            current_coin_account += Decimal(trade_item["bought"])
        if trade_item["sold"]:
            profit += Decimal(trade_item["sold"]) \
                * Decimal(trade_item["matecoin_price"])
            current_coin_account -= Decimal(trade_item["sold"])
    result = {
        "earned_money": str(profit),
        "matecoin_account": str(current_coin_account)
    }

    with open("profit.json", "w") as output_file:
        json.dump(result, output_file, indent=2)


calculate_profit("trades.json")
