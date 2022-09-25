import json
from decimal import Decimal


def calculate_profit(file_name: str):
    money_earned = 0
    money_spent = 0
    coins_earned = 0
    coins_spent = 0

    with open(file_name) as f:
        trades = json.load(f)

        for trade in trades:
            price = Decimal(trade["matecoin_price"])
            if trade["bought"]:
                money_spent += Decimal(trade["bought"]) * price
                coins_earned += Decimal(trade["bought"])
            if trade["sold"]:
                money_earned += Decimal(trade["sold"]) * price
                coins_spent += Decimal(trade["sold"])

        python_data = {
            "earned_money": str(money_earned - money_spent),
            "matecoin_account": str(coins_earned - coins_spent)
        }

    with open("profit.json", "w") as f:
        json.dump(python_data, f, indent=2)
