import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(trades_file, "r") as trades_file:
        trades = json.load(trades_file)
    for operation in trades:
        if operation["bought"]:
            matecoin_account += Decimal(operation["bought"])
            earned_money -= (Decimal(operation["bought"])
                             * Decimal(operation["matecoin_price"]))
        if operation["sold"]:
            matecoin_account -= Decimal(operation["sold"])
            earned_money += (Decimal(operation["sold"])
                             * Decimal(operation["matecoin_price"]))
    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
