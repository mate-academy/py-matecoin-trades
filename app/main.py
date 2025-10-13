import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(file_name: str) -> None:
    result = {}

    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade["bought"]:
            bought_value = Decimal(trade["bought"])
        else:
            bought_value = Decimal("0")

        if trade["sold"]:
            sold_value = Decimal(trade["sold"])
        else:
            sold_value = Decimal("0")

        matecoin_price_value = Decimal(trade["matecoin_price"])

        matecoin_account += bought_value
        matecoin_account -= sold_value

        earned_money -= (bought_value * matecoin_price_value)
        earned_money += (sold_value * matecoin_price_value)

    result["earned_money"] = str(earned_money)
    result["matecoin_account"] = str(matecoin_account)

    output_file_path = Path(__file__).resolve().parent.parent / "profit.json"

    with open(output_file_path, "r") as file:
        json.dump(result, file, indent=2)
