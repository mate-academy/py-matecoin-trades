import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as file:
        trades = json.load(file)
        bought_price = sum(
            Decimal(num["bought"]) * Decimal(num["matecoin_price"])
            for num in trades
            if num["bought"]
        )
        sold_price = sum(
            Decimal(num["sold"]) * Decimal(num["matecoin_price"])
            for num in trades
            if num["sold"]
        )
        bought_amount = sum(
            Decimal(num["bought"]) for num in trades if num["bought"]
        )
        sold_amount = sum(
            Decimal(num["sold"]) for num in trades if num["sold"]
        )
        res_dict = {
            "earned_money": str(sold_price - bought_price),
            "matecoin_account": str(bought_amount - sold_amount),
        }
    with open("profit.json", "w") as profit:
        json.dump(res_dict, profit, indent=2)
