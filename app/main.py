from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    profit = 0
    matecoins = 0
    with open(filename, "r") as file:
        trades_dict = json.load(file)
        for day in trades_dict:
            if day["bought"]:
                profit -= Decimal(
                    day["bought"]
                ) * Decimal(
                    day["matecoin_price"]
                )
                matecoins += Decimal(day["bought"])
            if day["sold"]:
                profit += Decimal(
                    day["sold"]
                ) * Decimal(
                    day["matecoin_price"]
                )
                matecoins -= Decimal(day["sold"])
            else:
                continue
    earned_dict = {"earned_money": str(profit),
                   "matecoin_account": str(matecoins)}
    with open("profit.json", "w") as file:
        json.dump(earned_dict, file, indent=2)
