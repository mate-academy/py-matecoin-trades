from decimal import Decimal

import json


def calculate_profit(json_file: str) -> None:
    with open(json_file, "r") as file:
        trades = json.load(file)
        count_money = 0
        count_metacoin = 0
        for trade in trades:
            if trade.get("bought"):
                count_money -= Decimal(trade.get("bought")
                                       ) * Decimal(trade["matecoin_price"])
                count_metacoin += Decimal(trade.get("bought"))
            if trade.get("sold"):
                count_money += Decimal(trade.get("sold")
                                       ) * Decimal(trade["matecoin_price"])
                count_metacoin -= Decimal(trade.get("sold"))
    with open("profit.json", "w") as input_file:
        json.dump(
            {
                "earned_money": str(count_money),
                "matecoin_account": str(count_metacoin)
            },
            input_file,
            indent=2
        )
