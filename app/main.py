import json
from decimal import Decimal


def calculate_profit(file_name: str = "trades.json") -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = 0
    matecoin_account = 0

    for deals_per_day in trades:
        if deals_per_day["bought"] is not None:
            matecoin_account += Decimal(deals_per_day["bought"])
            earned_money -= Decimal(deals_per_day["bought"]) * Decimal(
                deals_per_day["matecoin_price"]
            )
        if deals_per_day["sold"] is not None:
            matecoin_account -= Decimal(deals_per_day["sold"])
            earned_money += Decimal(deals_per_day["sold"]) * Decimal(
                deals_per_day["matecoin_price"]
            )

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
