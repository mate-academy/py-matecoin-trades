import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file, "r") as file:
        trades = json.load(file)

    total_spent = Decimal("0")
    total_earned = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought:
            total_spent += bought * matecoin_price
            matecoin_account += bought
        if sold:
            total_earned += sold * matecoin_price
            matecoin_account -= sold

    earned_money = total_earned - total_spent

    profit = {
        "earned_money": f"{earned_money:.7f}",
        "matecoin_account": f"{matecoin_account:.5f}"
    }

    with open(name_file, "w") as file_prof:
        json.dump(profit, file_prof, indent=2)
