import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
        count_money = Decimal("0")
        matecoin_account = Decimal("0")
        for trade in data:
            price = Decimal(trade["matecoin_price"])
            if trade["bought"] is not None:
                amount = Decimal(trade["bought"])
                matecoin_account += amount
                count_money -= amount * price

            if trade["sold"] is not None:
                amount = Decimal(trade["sold"])
                matecoin_account -= amount
                count_money += amount * price
        result = {
            "earned_money": str(count_money),
            "matecoin_account": str(matecoin_account),
        }
        with open("profit.json", "w") as f:
            json.dump(result, f, indent=2)
