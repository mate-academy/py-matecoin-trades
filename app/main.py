import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    with (open(name) as f):
        trade_data = json.load(f)
        profit = {
            "earned_money": 0,
            "matecoin_account": 0
        }
        for trade in trade_data:
            if trade["bought"]:
                profit["earned_money"] = profit["earned_money"] \
                    - (Decimal(trade["matecoin_price"])
                       * Decimal(trade["bought"]))
                profit["matecoin_account"] = profit["matecoin_account"] \
                    + Decimal(trade["bought"])
            if trade["sold"]:
                profit["earned_money"] = profit["earned_money"] \
                    + (Decimal(trade["matecoin_price"])
                       * Decimal(trade["sold"]))
                profit["matecoin_account"] -= Decimal(trade["sold"])

    json_format_profit = {key: str(profit[key]) for key in profit}

    with open("profit.json", "w") as f:
        json.dump(json_format_profit, f, indent=2)
