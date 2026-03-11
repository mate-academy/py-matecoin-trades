from decimal import Decimal
import json


def calculate_profit(data_file: str) -> None:
    with open(data_file, "r") as f:
        trades = json.load(f)
    sold_total = 0
    sold_total_price = 0
    bought_total = 0
    bought_total_price = 0
    for trade in trades:
        if trade["bought"]:
            bought_total += Decimal(trade["bought"])
            bought_total_price += (
                Decimal(trade["matecoin_price"]) * Decimal(trade["bought"])
            )
        if trade["sold"]:
            sold_total += Decimal(trade["sold"])
            sold_total_price += (
                Decimal(trade["matecoin_price"]) * Decimal(trade["sold"])
            )

    profit = {
        "earned_money": str(sold_total_price - bought_total_price),
        "matecoin_account": str(bought_total - sold_total)
    }
    print(profit)

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
