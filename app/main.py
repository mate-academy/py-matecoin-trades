import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    trades_dict = json.load(open(file_name))
    profit = Decimal("0")
    matecoin_balance = Decimal("0")
    for trade in trades_dict:
        if trade["bought"]:
            matecoin_balance += Decimal(trade["bought"])
            profit -= (Decimal(
                trade["bought"]
            ) * Decimal(
                trade["matecoin_price"]
            ))
        if trade["sold"]:
            matecoin_balance -= Decimal(trade["sold"])
            profit += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
        if not trade["bought"] and not trade["sold"]:
            continue
    matecoin_account_dict = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_balance)
    }
    with open("profit.json", "w") as profit_json_file:
        json.dump(matecoin_account_dict, profit_json_file, indent=2)
