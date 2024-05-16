import json
from decimal import Decimal


def calculate_profit(trades_file):
    with open(trades_file, "r") as file:
        trades = json.load(file)

    total_earned_money = Decimal(0)
    total_matecoin = Decimal(0)

    for trade in trades:
        bought = Decimal(trade["bought"]) if\
            "bought" in trade and trade["bought"] is not None else Decimal(0)
        sold = Decimal(trade["sold"]) if\
            "sold" in trade and trade["sold"] is not None else Decimal(0)
        price = Decimal(trade["matecoin_price"]) \
            if ("matecoin_price" in trade and trade["matecoin_price"]
                is not None) else Decimal(0)
        total_matecoin += bought - sold
        total_earned_money += (sold - bought) * price

    profit = {
        "earned_money": str(total_earned_money),
        "matecoin_account": str(total_matecoin)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
