import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        trades = json.load(f)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought_amount = Decimal(trade["bought"])
            earned_money = earned_money - price * bought_amount
            matecoin_account = matecoin_account + bought_amount
        if trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            earned_money = earned_money + price * sold_amount
            matecoin_account = matecoin_account - sold_amount
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }
    with open("profit.json", "w") as out_file:
        json.dump(result, out_file, indent=2)
