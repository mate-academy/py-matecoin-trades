from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades_data = json.load(f)

    total_bought = 0
    total_sold = 0
    total_bought_trades = 0
    total_sold_trades = 0

    for trade in trades_data:
        if trade["bought"]:
            total_bought += Decimal(trade["bought"])
            total_bought_trades += Decimal(trade["bought"]) * Decimal(
                trade["matecoin_price"]
            )
        if trade["sold"]:
            total_sold += Decimal(trade["sold"])
            total_sold_trades += Decimal(trade["sold"]) * Decimal(
                trade["matecoin_price"]
            )

    earned_money = str(total_sold_trades - total_bought_trades)
    matecoin_account = str(total_bought - total_sold)

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as n:
        json.dump(profit, n, indent=2)
