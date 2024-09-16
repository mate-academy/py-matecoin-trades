import decimal
import json


def calculate_profit(name_of_file: str):
    with open(name_of_file, "r") as trades:
        trades_data = json.load(trades)

    profit_data = {
        "earned_money": 0,
        "matecoin_account": 0
    }
    for trade in trades_data:
        price = decimal.Decimal(trade["matecoin_price"])
        bought = decimal.Decimal(trade["bought"]) if trade["bought"] else 0
        sold = decimal.Decimal(trade["sold"]) if trade["sold"] else 0

        profit_data["matecoin_account"] += bought - sold
        profit_data["earned_money"] -= (bought - sold) * price

    with open("profit.json", "w") as profit:
        json.dump(profit_data, profit, indent=2)
