import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(f"{file_name}", "r") as file:
        trades = json.load(file)

    profit_info = {
        "earned_money": "0.0",
        "matecoin_account": "0.0"
    }
    for i in trades:
        if i["bought"] is not None:
            profit_info["earned_money"] = (
                str(Decimal(profit_info["earned_money"])
                    - Decimal(i["matecoin_price"])
                    * Decimal(i["bought"])))
            profit_info["matecoin_account"] = (
                str(Decimal(profit_info["matecoin_account"])
                    + Decimal(i["bought"])))

        if i["sold"] is not None:
            profit_info["earned_money"] = (
                str(Decimal(profit_info["earned_money"])
                    + Decimal(i["matecoin_price"])
                    * Decimal(i["sold"])))
            profit_info["matecoin_account"] = (
                str(Decimal(profit_info["matecoin_account"])
                    - Decimal(i["sold"])))

    with open("profit.json", "w") as file:
        json.dump(profit_info, file, indent=2)
