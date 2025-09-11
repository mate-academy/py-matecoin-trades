import json
import os
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit_dict = {}
    with open(file_name, "r") as file:
        trades = json.load(file)

    result_bought = 0
    result_sell = 0
    matecoin_bought = 0
    matecoin_sell = 0
    for trade in trades:
        if trade.get("bought") is not None:
            result = (Decimal(trade["bought"])
                      * Decimal(trade["matecoin_price"]))
            result_bought += result
            matecoin_bought += Decimal(trade["bought"])
        if trade.get("sold") is not None:
            result = Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            result_sell += result
            matecoin_sell += Decimal(trade["sold"])

    if not profit_dict.get("earned_money"):
        profit_dict["earned_money"] = str(result_sell - result_bought)
    if not profit_dict.get("matecoin_account"):
        profit_dict["matecoin_account"] = str(matecoin_bought - matecoin_sell)
    if not os.path.exists("profit.jason"):
        with open("profit.json", "w") as file:
            json.dump(profit_dict, file, indent=2)
