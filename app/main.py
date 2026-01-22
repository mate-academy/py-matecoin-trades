import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with (open(trades_file, "r") as reda_file):
        trades_data = json.load(reda_file)
        for transaction in trades_data:
            if transaction["bought"]:
                matecoin_account += Decimal(transaction["bought"])
                earned_money -= (Decimal(transaction["bought"])
                                 * Decimal(transaction["matecoin_price"]))
            if transaction["sold"]:
                matecoin_account -= Decimal(transaction["sold"])
                earned_money += (Decimal(transaction["sold"])
                                 * Decimal(transaction["matecoin_price"]))
    profit_data = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as write_file:
        json.dump(profit_data, write_file, indent=2)
