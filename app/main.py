import json
from decimal import Decimal


def calculate_profit(name: json) -> None:
    with open(name, "r") as file:
        trades = json.load(file)
        matecoin_account = Decimal("0")
        total_spent = Decimal("0")
        total_gained = Decimal("0")
        for trade in trades:
            if trade["bought"] is not None:
                matecoin_account += Decimal(trade["bought"])
                total_spent += (Decimal(trade["matecoin_price"])
                                * Decimal(trade["bought"]))
            if trade["sold"] is not None:
                matecoin_account -= Decimal(trade["sold"])
                total_gained += (Decimal(trade["sold"])
                                 * Decimal(trade["matecoin_price"]))
        earned_money = Decimal(total_gained) - Decimal(total_spent)
        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }
        with open("profit.json", "w") as file:
            json.dump(profit, file, indent=2)
