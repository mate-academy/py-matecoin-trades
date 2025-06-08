from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    earned_money, matecoin_account = Decimal("0"), Decimal("0")

    with open(file_name, "r") as file:
        trades = json.load(file)
        for trade in trades:
            if trade["bought"] is not None:
                earned_money -= (Decimal(trade["bought"])
                                 * Decimal(trade["matecoin_price"]))
                matecoin_account += Decimal(trade["bought"])
            if trade["sold"] is not None:
                earned_money += (Decimal(trade["sold"])
                                 * Decimal(trade["matecoin_price"]))
                matecoin_account -= Decimal(trade["sold"])

    with open("profit.json", "w") as file:
        data = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(data, file, indent=4)
