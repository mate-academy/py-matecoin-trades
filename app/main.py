from decimal import Decimal
import json


def calculate_profit(trades_file_name: str) -> None:
    with open(trades_file_name, "r") as trades_file:
        trades = json.load(trades_file)

    total_bought_money = Decimal("0")
    total_sold_money = Decimal("0")
    total_bought_volume = Decimal("0")
    total_sold_volume = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_volume = Decimal(trade["bought"])
            total_bought_volume += bought_volume
            total_bought_money += bought_volume * price

        if trade["sold"] is not None:
            sold_volume = Decimal(trade["sold"])
            total_sold_volume += sold_volume
            total_sold_money += sold_volume * price

    earned_money = total_sold_money - total_bought_money
    matecoin_account = total_bought_volume - total_sold_volume

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file, indent=2)
