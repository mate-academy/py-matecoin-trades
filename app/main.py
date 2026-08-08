import json

from decimal import Decimal


def calculate_profit(filename: str) -> None:
    spent_money = Decimal("0")
    bought_coins = Decimal("0")
    earned_money = Decimal("0")
    sold_coins = Decimal("0")
    with open(filename) as f:
        trades_data = json.load(f)
    # print(trades_data)
    for dictionary in trades_data:
        if dictionary["bought"]:
            spent_money += (
                Decimal(dictionary["bought"])
                * Decimal(dictionary["matecoin_price"])
            )
            bought_coins += Decimal(dictionary["bought"])
        if dictionary["sold"]:
            earned_money += (
                Decimal(dictionary["sold"])
                * Decimal(dictionary["matecoin_price"])
            )
            sold_coins += Decimal(dictionary["sold"])

    profit_data = {
        "earned_money": str(earned_money - spent_money),
        "matecoin_account": str(bought_coins - sold_coins),
    }
    print(profit_data)
    with open("profit.json", "w") as profit_file:
        json.dump(profit_data, profit_file, indent=2)
