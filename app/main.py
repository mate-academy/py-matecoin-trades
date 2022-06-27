import json
from decimal import Decimal


def calculate_profit(file_name: str):
    with open(file_name, "r") as json_type:
        trades = json.load(json_type)
    total_bought = 0
    bought_in_money = 0
    total_sold = 0
    sold_in_money = 0
    for trade in trades:
        if trade["bought"] is not None:
            total_bought += Decimal(trade["bought"])
            bought_in_money += \
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
        if trade["sold"] is not None:
            total_sold += Decimal(trade["sold"])
            sold_in_money += \
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
    profit = {"earned_money": str(sold_in_money - bought_in_money),
              "matecoin_account": str(total_bought - total_sold)}
    with open("profit.json", "w") as json_file:
        json.dump(profit, json_file, indent=2)
