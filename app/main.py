from decimal import Decimal
import json


def calculate_profit(file_name: json) -> None:
    with open(file_name) as file:
        trades = json.load(file)

    bought = Decimal("0")
    sold = Decimal("0")
    matecoin_balance = Decimal("0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought += Decimal(trade["bought"]) * matecoin_price
            matecoin_balance += Decimal(trade["bought"])

        if trade["sold"] is not None:
            sold += Decimal(trade["sold"]) * matecoin_price
            matecoin_balance -= Decimal(trade["sold"])

    earned_money = sold - bought

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_balance)
    }

    with open("profit.json", "w") as file_json:
        json.dump(result, file_json, indent=2)
