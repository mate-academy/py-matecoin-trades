import decimal
import json


def calculate_profit(file_name: str) -> None:
    profit_info = {
        "earned_money": decimal.Decimal("0.0"),
        "matecoin_account": decimal.Decimal("0.0"),
    }

    with open(file_name, "r") as file:
        crypto_info = json.load(file)

    for day in crypto_info:
        if day["bought"]:
            profit_info["matecoin_account"] += decimal.Decimal(day["bought"])
            profit_info["earned_money"] -= (
                decimal.Decimal(day["bought"])
                * decimal.Decimal(day["matecoin_price"])
            )
        if day["sold"]:
            profit_info["matecoin_account"] -= decimal.Decimal(day["sold"])
            profit_info["earned_money"] += (
                decimal.Decimal(day["sold"])
                * decimal.Decimal(day["matecoin_price"])
            )

    profit_info["earned_money"] = str(profit_info["earned_money"])
    profit_info["matecoin_account"] = str(profit_info["matecoin_account"])

    with open("profit.json", "w") as profit:
        json.dump(profit_info, profit, indent=2)
