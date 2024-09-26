import json
from decimal import Decimal


def calculate_profit(trades: json) -> None:
    with open(trades, "r") as file_in:
        trades_list = json.load(file_in)
    earned_money = 0
    account_balance = 0
    for trade in trades_list:
        if trade["bought"] is None:
            trade["bought"] = 0
        if trade["sold"] is None:
            trade["sold"] = 0
        earned_money += (
            (Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
             - Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])))
        account_balance += Decimal(trade["bought"]) - Decimal(trade["sold"])
    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(account_balance)}
    with open("profit.json", "w") as file_out:
        json.dump(profit_dict, file_out, indent=2)
