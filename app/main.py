from decimal import Decimal
import json


def calculate_profit(json_file: str) -> None:
    with open(json_file, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trades:
        if trade["bought"]:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
        if trade["sold"]:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))

    with open("profit.json", "w") as f:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            }, f, indent=2)
