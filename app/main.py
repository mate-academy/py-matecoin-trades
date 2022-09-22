import json
from decimal import Decimal


def calculate_profit(file):
    with open(file, "r") as f:
        trades = json.load(f)
    result = {"earned_money": 0, "matecoin_account": 0}
    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is None:
            sold = Decimal(trade["sold"])
            result["earned_money"] += sold * price
            result["matecoin_account"] -= sold
        elif trade["sold"] is None:
            bought = Decimal(trade["bought"])
            result["earned_money"] -= bought * price
            result["matecoin_account"] += bought
        else:
            bought = Decimal(trade["bought"])
            sold = Decimal(trade["sold"])
            result["earned_money"] += (sold - bought) * price
            result["matecoin_account"] += bought - sold
    result["earned_money"] = str(result["earned_money"])
    result["matecoin_account"] = str(result["matecoin_account"])
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
