import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades_info = json.load(file)
    profit = {"earned_money": Decimal("0"), "matecoin_account": Decimal("0")}

    for trade_info in trades_info:
        if trade_info["bought"] is not None:
            profit["earned_money"] -= (Decimal(trade_info["bought"])
                                       * Decimal(trade_info["matecoin_price"]))
            profit["matecoin_account"] += Decimal(trade_info["bought"])
        if trade_info["sold"] is not None:
            profit["earned_money"] += (Decimal(trade_info["sold"])
                                       * Decimal(trade_info["matecoin_price"]))
            profit["matecoin_account"] -= Decimal(trade_info["sold"])

    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
