from decimal import Decimal
import json


def calculate_profit(name: str):
    sum_doll = 0
    mate_coin = 0
    with open(name, "r") as f:
        trades_info = json.load(f)

    for trade in trades_info:
        coin_price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            mate_coin += Decimal(trade["bought"])
            sum_doll -= Decimal(trade["bought"]) * coin_price
        else:
            mate_coin -= Decimal(trade["sold"])
            sum_doll += Decimal(trade["sold"]) * coin_price

    result = {
        "earned_money": str(sum_doll),
        "matecoin_account": str(mate_coin)
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
