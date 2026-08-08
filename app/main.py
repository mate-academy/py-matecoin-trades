import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as file:
        trades_info = json.load(file)
    profit_dict = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }
    for trade in trades_info:
        if trade["bought"]:
            profit_dict["matecoin_account"] += Decimal(trade["bought"])
            profit_dict["earned_money"] -= (Decimal(trade["bought"])
                                            * Decimal(trade["matecoin_price"]))
        if trade["sold"]:
            profit_dict["matecoin_account"] -= Decimal(trade["sold"])
            profit_dict["earned_money"] += (Decimal(trade["sold"])
                                            * Decimal(trade["matecoin_price"]))
    profit_dict["earned_money"] = str(profit_dict["earned_money"])
    profit_dict["matecoin_account"] = str(profit_dict["matecoin_account"])
    with open("profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2)
