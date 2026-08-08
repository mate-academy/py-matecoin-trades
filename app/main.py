import json
from decimal import Decimal


def calculate_profit(json_file: str) -> None:
    with (open(json_file, "r") as f):
        json_datan = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade_order in json_datan:
        matecoin_price = Decimal(trade_order["matecoin_price"])
        if trade_order["bought"] is not None:
            bought_volume = Decimal(trade_order["bought"])
            cost = bought_volume * matecoin_price
            matecoin_account += bought_volume
            earned_money -= cost

        if trade_order["sold"] is not None:
            sold_value = Decimal(trade_order["sold"])
            profit = sold_value * matecoin_price
            matecoin_account -= sold_value
            earned_money += profit

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
