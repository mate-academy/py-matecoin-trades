from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    profit = 0
    mate_coin_amount = 0
    with (open(filename) as file):
        data = json.load(file)
        for trade in data:
            if trade["bought"]:
                profit -= (Decimal(trade["bought"])
                           * Decimal(trade["matecoin_price"]))
                mate_coin_amount += Decimal(trade["bought"])
            if trade["sold"]:
                profit += (Decimal(trade["sold"])
                           * Decimal(trade["matecoin_price"]))
                mate_coin_amount -= Decimal(trade["sold"])

    with open(
            "profit.json",
            "w"
    ) as file:
        result_string = {
            "earned_money": str(profit),
            "matecoin_account": str(mate_coin_amount)
        }
        json.dump(result_string, file, indent=2)
