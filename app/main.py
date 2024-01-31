import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open("app/trades.json", "r") as f:
        trades = json.load(f)

    matecoin_account = Decimal("0")
    money_spent = Decimal("0")
    money_earned = Decimal("0")

    for trade in trades:
        if trade["bought"]:
            volume_bought = Decimal(trade["bought"])
            matecoin_account += volume_bought
            money_spent += volume_bought * Decimal(trade["matecoin_price"])

        if trade["sold"]:
            volume_sold = Decimal(trade["sold"])
            matecoin_account -= volume_sold
            money_earned += volume_sold * Decimal(trade["matecoin_price"])

    earned_money = money_earned - money_spent

    income = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(income, f, indent=2)
