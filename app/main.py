import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file) as f:
        trades_data = json.load(f)
        temp = {
            "current_account": 0,
            "earned_money": 0
        }

        for trade in trades_data:
            if trade["bought"]:
                temp["current_account"] += Decimal(trade["bought"])
                temp["earned_money"] -= (Decimal(trade["bought"])
                                         * Decimal(trade["matecoin_price"]))
            if trade["sold"]:
                temp["current_account"] -= Decimal(trade["sold"])
                temp["earned_money"] += (Decimal(trade["sold"])
                                         * Decimal(trade["matecoin_price"]))
    result = {
        "earned_money": str(temp["earned_money"]),
        "matecoin_account": str(temp["current_account"])
    }
    with open("profit.json", "w") as f2:
        json.dump(result, f2, indent=2)
