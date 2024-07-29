import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    total_profit = Decimal("0")
    total_coins = Decimal("0")
    for trade in trades:
        if "bought" in trade and trade["bought"] is not None:
            coins_bought = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            total_coins += coins_bought
            total_profit -= coins_bought * price
        if "sold" in trade and trade["sold"] is not None:
            coins_sold = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            total_coins -= coins_sold
            total_profit += coins_sold * price
    result = {"earned_money": str(total_profit),
              "matecoin_account": str(total_coins),
              }
    with open("profit.json", "w") as file:
        json.dump(result, file, default=str, indent=2)
