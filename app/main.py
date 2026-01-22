from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        trader_data = json.load(f)

    profit = {
        "bought": Decimal(0),
        "sold": Decimal(0),
        "account": Decimal(0)
    }

    for current_data in trader_data:
        if current_data["bought"]:
            profit["account"] += Decimal(current_data["bought"])
            profit["bought"] += (
                Decimal(current_data["matecoin_price"])
                * Decimal(current_data["bought"])
            )

        if current_data["sold"]:
            profit["account"] -= Decimal(current_data["sold"])
            profit["sold"] += (
                Decimal(current_data["matecoin_price"])
                * Decimal(current_data["sold"])
            )

    earned = profit["sold"] - profit["bought"]

    result_dict = {
        "earned_money": str(earned),
        "matecoin_account": str(profit["account"])
    }

    with open("profit.json", "w") as f:
        json.dump(result_dict, f, indent=2)
