import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    total_cost = Decimal("0")
    total_revenue = Decimal("0")
    total_bought = Decimal("0")
    total_sold = Decimal("0")
    with open(trades_file, "r") as json_file:
        trades = json.load(json_file)
    for trade in trades:
        if trade["bought"]:
            bought_volume = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            total_cost += bought_volume * matecoin_price
            total_bought += bought_volume

        if trade["sold"]:
            sold_volume = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            total_revenue += sold_volume * matecoin_price
            total_sold += sold_volume

    total_profit = total_revenue - total_cost
    total_matecoin = total_bought - total_sold

    output_data = {
        "earned_money": str(total_profit),
        "matecoin_account": str(total_matecoin),
    }

    with open("profit.json", "w") as profit_json:
        json.dump(output_data, profit_json, indent=2)
