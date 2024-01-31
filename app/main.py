import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file, "r") as file:
        trade_info = json.load(file)
        # print(trade_info)
    # spend
    earned_money = Decimal("0.0")
    # last
    matecoin_account = Decimal("0.0")

    for trade in trade_info:
        if trade["bought"] is not None:
            bought_amount = Decimal(trade["bought"])
            bought_cost = bought_amount * Decimal(trade["matecoin_price"])
            earned_money -= bought_cost
            matecoin_account += bought_amount

        if trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            sold_cost = sold_amount * Decimal(trade["matecoin_price"])
            earned_money += sold_cost
            matecoin_account -= sold_amount

    with open("profit.json", "w") as f:
        json.dump({
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }, f, indent=2)
# calculate_profit("trades.json")
