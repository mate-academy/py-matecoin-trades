import json
from decimal import Decimal


def calculate_profit(file_name: str = "trades.json") -> None:
    with open(file_name, "r") as file:
        trades_data = json.load(file)

    earned_money = 0
    matecoin_account = 0

    for deal in trades_data:
        if deal["bought"] is not None:
            matecoin_account += Decimal(deal["bought"])
            earned_money -= Decimal(deal["bought"]) * Decimal(
                deal["matecoin_price"]
            )
        if deal["sold"] is not None:
            matecoin_account -= Decimal(deal["sold"])
            earned_money += Decimal(deal["sold"]) * Decimal(
                deal["matecoin_price"]
            )

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
