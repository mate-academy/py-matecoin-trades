import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as input_file:
        loading = json.load(input_file)
        info = {"bought1": 0, "sold1": 0, "earned_bought": 0, "earned_sold": 0}
        for element in loading:
            buy = element["bought"]
            price = element["matecoin_price"]
            if buy is not None:
                info["bought1"] += Decimal(buy)
                info["earned_bought"] += Decimal(buy) * Decimal(price)

            sell = element["sold"]
            if sell is not None:
                info["sold1"] += Decimal(sell)
                info["earned_sold"] += Decimal(sell) * Decimal(price)

        progress = Decimal(info["earned_sold"]) - Decimal(info["earned_bought"])
        meta = Decimal(info["bought1"]) - Decimal(info["sold1"])
        res = {
            "earned_money": str(progress),
            "matecoin_account": str(meta)
        }

    with open("profit.json", "w") as output_file:
        json.dump(res, output_file, indent=2)
