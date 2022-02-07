import json


def calculate_profit(name_of_file: str):
    with open(name_of_file, "r") as trades:
        trades_data = json.load(trades)

    profit_data = {
        "earned_money": 0,
        "matecoin_account": 0
    }
    for trade in trades_data:
        price = float(trade["matecoin_price"])
        if trade["bought"] and trade["sold"]:
            bought = float(trade["bought"])
            sold = float(trade["sold"])
        elif not trade["bought"] and trade["sold"]:
            bought = 0
            sold = float(trade["sold"])
        elif not trade["sold"] and trade["bought"]:
            bought = float(trade["bought"])
            sold = 0

        profit_data["matecoin_account"] += bought - sold
        profit_data["earned_money"] -= (bought - sold) * price

    with open("profit.json", "w") as profit:
        json.dump(profit_data, profit, indent=2)
