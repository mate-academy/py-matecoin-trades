import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as json_file:
        data = json.load(json_file)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in data:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_amount = Decimal(trade["bought"])
            matecoin_account += bought_amount
            earned_money -= bought_amount * price

        if trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            matecoin_account -= sold_amount
            earned_money += sold_amount * price

    result_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as final_file:
        json.dump(result_dict, final_file, indent=2)
