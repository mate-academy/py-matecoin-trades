import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        data = json.load(f)

    bought_coins = Decimal("0")
    sold_coins = Decimal("0")
    total_costs = Decimal("0")
    total_sales = Decimal("0")

    for trade in data:
        metacoins_price = Decimal(str(trade["matecoin_price"]))
        if trade["bought"]:
            num_bought_coins = Decimal(str(trade["bought"]))
            bought_coins += num_bought_coins
            total_costs += metacoins_price * num_bought_coins
        if trade["sold"]:
            num_sold_coins = Decimal(str(trade["sold"]))
            sold_coins += num_sold_coins
            total_sales -= metacoins_price * num_sold_coins

    result = {}
    result["earned_money"] = str(-total_costs - total_sales)
    result["matecoin_account"] = str(bought_coins - sold_coins)

    with open("profit.json", "w") as p:
        json.dump(result, p, indent=2)
