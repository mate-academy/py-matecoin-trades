import json
from decimal import Decimal


def calculate_profit(trades_file: json) -> None:
    money = Decimal(0)
    matecoin = Decimal(0)

    with open(trades_file, "r") as file:
        trades = json.load(file)

    for trade in trades:
        bought = Decimal(trade["bought"]) if\
            "bought" in trade and trade["bought"] is not None else Decimal(0)
        sold = Decimal(trade["sold"]) if\
            "sold" in trade and trade["sold"] is not None else Decimal(0)
        price = Decimal(trade["matecoin_price"]) \
            if ("matecoin_price" in trade and trade["matecoin_price"]
                is not None) else Decimal(0)
        money += (sold - bought) * price
        matecoin += bought - sold

    profit = {
        "earned_money": str(money),
        "matecoin_account": str(matecoin)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
