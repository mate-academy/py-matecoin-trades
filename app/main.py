import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    total_usd = 0
    total_mc = 0
    for trade in trades:
        if trade["sold"] is not None:
            trade_sum = Decimal(trade["matecoin_price"]) * Decimal(
                trade["sold"])
            total_usd += trade_sum
            total_mc -= Decimal(trade["sold"])
        if trade["bought"] is not None:
            trade_sum = Decimal(trade["matecoin_price"]) * Decimal(
                trade["bought"])
            total_usd -= trade_sum
            total_mc += Decimal(trade["bought"])

    result = {
        "earned_money": str(total_usd),
        "matecoin_account": str(total_mc)
    }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
