import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as file:
        info = json.load(file)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for process in info:
        if process["bought"] is not None:
            earned_money -= (Decimal(process["bought"])
                             * Decimal(process["matecoin_price"]))
            matecoin_account += Decimal(process["bought"])

        if process["sold"] is not None:
            earned_money += (Decimal(process["sold"])
                             * Decimal(process["matecoin_price"]))
            matecoin_account -= Decimal(process["sold"])

    profit_info = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit:
        json.dump(profit_info, profit, indent=2)
