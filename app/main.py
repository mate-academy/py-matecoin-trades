import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought_volume = Decimal(trade["bought"])
            cost = bought_volume * matecoin_price
            earned_money -= cost
            matecoin_account += bought_volume
        elif trade["sold"] is not None:
            sold_volume = Decimal(trade["sold"])
            revenue = sold_volume * matecoin_price
            earned_money += revenue
            matecoin_account -= sold_volume

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit_data, f)


calculate_profit("file")
