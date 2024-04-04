import json
from decimal import Decimal as Dec


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades_data = json.load(file)

    profit = {
        "earned_money": "0",
        "matecoin_account": "0"
    }

    for des in trades_data:
        if des["bought"] is not None:
            cost_b = Dec(des["bought"]) * Dec(des["matecoin_price"])
            profit["earned_money"] = str(Dec(profit["earned_money"]) - cost_b)
            profit["matecoin_account"] = str(Dec(profit["matecoin_account"])
                                             + Dec(des["bought"]))
        if des["sold"] is not None:
            cost_s = Dec(des["sold"]) * Dec(des["matecoin_price"])
            profit["earned_money"] = str(Dec(profit["earned_money"]) + cost_s)
            profit["matecoin_account"] = str(Dec(profit["matecoin_account"])
                                             - Dec(des["sold"]))

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
