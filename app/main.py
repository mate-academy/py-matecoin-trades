from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        trades = json.load(f)

    bought = 0
    bought_count = 0
    sold = 0
    sold_count = 0

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought += Decimal(trade["bought"]) * price
            bought_count += Decimal(trade["bought"])
        if trade["sold"] is not None:
            sold += Decimal(trade["sold"]) * price
            sold_count += Decimal(trade["sold"])

    earned_money = sold - bought
    matecoin_account = bought_count - sold_count

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
