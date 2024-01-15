from decimal import Decimal
import json


def calculate_profit(json_file: str,) -> None:
    with open(json_file, "r") as file:
        trades = json.load(file)
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")
    for trade in trades:
        if trade["bought"] is not None:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
        if trade["sold"] is not None:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
