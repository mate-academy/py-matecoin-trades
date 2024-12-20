import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    sold_count_all_in_dollars = 0
    sold_count = 0
    bought_count_all_in_dollars = 0
    bought_count = 0

    for trade in trades:
        if trade["bought"] is None:
            sold_count_all_in_dollars += Decimal(trade["sold"]) * Decimal(
                trade["matecoin_price"]
            )
            sold_count += Decimal(trade["sold"])
        if trade["sold"] is None:
            bought_count_all_in_dollars += Decimal(trade["bought"]) * Decimal(
                trade["matecoin_price"]
            )
            bought_count += Decimal(trade["bought"])

    result_dict = {
        "earned_money": str(sold_count_all_in_dollars
                            - bought_count_all_in_dollars),
        "matecoin_account": str(sold_count - bought_count),
    }

    with open("profit.json", "w") as file:
        json.dump(result_dict, file, indent=2)
