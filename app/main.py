import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file) as f:
        trades = json.load(f)

    matecoin_account = 0
    money_spent = 0
    money_earned = 0

    for trade in trades:
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            money_spent += bought * Decimal(trade["matecoin_price"])
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            money_earned += sold * Decimal(trade["matecoin_price"])

    earned_money = money_earned - money_spent

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
