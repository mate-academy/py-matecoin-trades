import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as source_file:
        trades = json.load(source_file)

    trades = [
        {
            key: ("0" if value is None else value)
            for key, value in trade.items()
        }
        for trade in trades
    ]

    bought_total_coins = sum(
        Decimal(trade["bought"]) - Decimal(trade["sold"])
        for trade in trades
    )

    bought_total = sum(
        Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
        for trade in trades
    )
    sold_total = sum(
        Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
        for trade in trades
    )

    profit = {
        "earned_money": f"{sold_total - bought_total}",
        "matecoin_account": f"{bought_total_coins}"
    }

    with open("profit.json", "w") as output_file:
        json.dump(profit, output_file, indent=2)
