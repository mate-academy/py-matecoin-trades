import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades_dicts = json.load(file)
        bought_sum = Decimal("0")
        sale_sum = Decimal("0")
        matecoin_account = Decimal("0")
        for trade in trades_dicts:
            price = Decimal(trade["matecoin_price"])
            if trade["bought"] is not None:
                bought_sum += Decimal(trade["bought"]) * price
                matecoin_account += Decimal(trade["bought"])
            if trade["sold"] is not None:
                sale_sum += Decimal(trade["sold"]) * price
                matecoin_account -= Decimal(trade["sold"])
        earned_money = sale_sum - bought_sum
        final_dict = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
    with open("profit.json", "w") as file:
        json.dump(final_dict, file, indent=2)
