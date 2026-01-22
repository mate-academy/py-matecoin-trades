import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    money_earned = 0
    money_spent = 0
    coins_earned = 0
    coins_spent = 0

    with open(file_name) as f:
        trades = json.load(f)

        for deal in trades:
            price = Decimal(deal["matecoin_price"])
            if deal["bought"]:
                money_spent += Decimal(deal["bought"]) * price
                coins_earned += Decimal(deal["bought"])
            if deal["sold"]:
                money_earned += Decimal(deal["sold"]) * price
                coins_spent += Decimal(deal["sold"])

        information = {
            "earned_money": str(money_earned - money_spent),
            "matecoin_account": str(coins_earned - coins_spent)
        }

    with open("profit.json", "w") as f:
        json.dump(information, f, indent=2)
