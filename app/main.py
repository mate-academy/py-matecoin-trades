from decimal import Decimal
import json


def calculate_profit(trades_info_file: str):
    with open(trades_info_file, "r") as file:
        trades_data = json.load(file)

    profit_data = {
        "earned_money": Decimal(0),
        "matecoin_account": Decimal(0)
    }

    for trade in trades_data:
        if trade["bought"] is not None:
            profit_data["matecoin_account"] += Decimal(trade["bought"])
            costs = Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            profit_data["earned_money"] -= costs

        if trade["sold"] is not None:
            profit_data["matecoin_account"] -= Decimal(trade["sold"])
            costs = Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            profit_data["earned_money"] += costs

    profit_data = {
        key: str(value) for key, value in profit_data.items()
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
