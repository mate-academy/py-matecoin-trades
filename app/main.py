import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    trade: dict
    matecoin_account = 0
    earned_money = 0
    with open(name_file, "r") as file:
        trades: list = json.load(file)
    for trade_day in trades:
        if trade_day["bought"]:
            matecoin_account += Decimal(trade_day["bought"])
            earned_money += (Decimal(trade_day["matecoin_price"])
                             * Decimal(trade_day["bought"]))
        if trade_day["sold"]:
            matecoin_account -= Decimal(trade_day["sold"])
            earned_money -= (Decimal(trade_day["matecoin_price"])
                             * Decimal(trade_day["sold"]))
    trade = {"earned_money": str(-earned_money),
             "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as file:
        json.dump(trade, file, indent=2)
