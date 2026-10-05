import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        trades = json.load(f)
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")
    for trade in trades:
        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account += amount
            earned_money -= amount * price
        if trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            sold_price = Decimal(trade["matecoin_price"])
            matecoin_account -= sold_amount
            earned_money += sold_price * sold_amount

    result_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }
    with open("profit.json", "w") as f:
        json.dump(result_dict, f, indent=2)
