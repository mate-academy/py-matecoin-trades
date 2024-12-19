import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    sold_count_all_in_dollars = sum(
        [
            Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            for trade in trades
            if trade["bought"] is None
        ]
    )
    bought_count_all_in_dollars = sum(
        [
            Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            for trade in trades
            if trade["sold"] is None
        ]
    )

    sold_count = sum(
        [Decimal(trade["sold"]) for trade in trades if trade["bought"] is None]
    )
    bought_count = sum(
        [Decimal(trade["bought"]) for trade in trades if trade["sold"] is None]
    )

    result_dict = {
        "earned_money": str(sold_count_all_in_dollars
                            - bought_count_all_in_dollars),
        "matecoin_account": str(bought_count - sold_count),
    }

    with open("profit.json", "w") as file:
        json.dump(result_dict, file)
