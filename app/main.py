import json
from decimal import Decimal as Decimal


def calculate_profit(trade_file: str) -> None:
    profit = {
        "earned_money": Decimal(0),
        "matecoin_account": Decimal(0)
    }
    with open(trade_file, "r") as f:
        trades = json.load(f)
        for i in trades:
            if i["sold"]:
                profit["earned_money"] += Decimal(i["sold"]) * Decimal(
                    i["mate-coin_price"])
                profit["matecoin_account"] -= Decimal(i["sold"])
            if i["bought"]:
                profit["earned_money"] -= Decimal(i["bought"]) * Decimal(
                    i["matecoin_price"])
                profit["matecoin_account"] += Decimal(i["bought"])

    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
