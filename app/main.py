import json
from decimal import Decimal


def calculate_profit(input_file: str) -> None:
    with open(input_file, "r") as f:
        trades = json.load(f)

    total_earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        if trade["bought"] is not None:
            bought_volume = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            total_earned_money -= bought_volume * matecoin_price
            matecoin_account += bought_volume

        if trade["sold"] is not None:
            sold_volume = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            total_earned_money += sold_volume * matecoin_price
            matecoin_account -= sold_volume

    result = {
        "earned_money": str(total_earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
