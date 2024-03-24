import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit_data = {"earned_money": Decimal("0"),
                   "matecoin_account": Decimal("0")}
    with (open(file_name, "r") as file):
        file_date = json.load(file)

        for day in file_date:
            if day["bought"]:
                profit_data["matecoin_account"] += Decimal(day["bought"])
                profit_data["earned_money"] -= Decimal(
                    day["matecoin_price"]) * Decimal(day["bought"])
            if day["sold"]:
                profit_data["matecoin_account"] -= Decimal(day["sold"])
                profit_data["earned_money"] += Decimal(
                    day["matecoin_price"]) * Decimal(day["sold"])

    profit_data["earned_money"] = str(profit_data["earned_money"])
    profit_data["matecoin_account"] = str(profit_data["matecoin_account"])

    with open("profit.json", "w") as file_profit:
        json.dump(profit_data, file_profit, indent=2)
