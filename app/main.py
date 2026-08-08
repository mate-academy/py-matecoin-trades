import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as source_file:
        trades = json.load(source_file)
    matecoin_account = Decimal("0")
    profit = Decimal("0")
    for trade in trades:
        if trade["bought"]:
            matecoin_account += Decimal(trade["bought"])
            profit -= (Decimal(trade["bought"])
                       * Decimal(trade["matecoin_price"]))
        if trade["sold"]:
            matecoin_account -= Decimal(trade["sold"])
            profit += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
    profit_dict = {"earned_money": str(profit),
                   "matecoin_account": str(matecoin_account)}
    print(profit_dict)
    with open("profit.json", "a") as file_out:
        json.dump(profit_dict, file_out, indent=2)
