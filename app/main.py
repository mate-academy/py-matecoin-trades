import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    earned_money = 0
    matecoin_account = 0

    for trade in trades:
        if trade["bought"]:
            deal_amount = Decimal(trade["bought"])
            earned_money -= (deal_amount * Decimal(trade["matecoin_price"]))
            matecoin_account += deal_amount

        if trade["sold"]:
            deal_amount = Decimal(trade["sold"])
            earned_money += (deal_amount * Decimal(trade["matecoin_price"]))
            matecoin_account -= deal_amount

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as outfile:
            json.dump(result, outfile, indent=2)
