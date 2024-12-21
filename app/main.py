import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    total_spent = total_earned = matecoin_balance = Decimal("0.0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"]:

            total_spent += Decimal(trade["bought"]) * price
            matecoin_balance += Decimal(trade["bought"])

        if trade["sold"]:

            total_earned += Decimal(trade["sold"]) * price
            matecoin_balance -= Decimal(trade["sold"])

    profit_data = {
        "earned_money": str(total_earned - total_spent),
        "matecoin_account": str(matecoin_balance)
    }

    with open("profit.json", "w") as outfile:
        json.dump(profit_data, outfile, indent=2)
