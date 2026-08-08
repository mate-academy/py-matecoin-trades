import json
from decimal import Decimal


def calculate_profit(file_trade: json) -> None:
    profit = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    with open(file_trade) as opened_file:
        trades = json.load(opened_file)
        for trade in trades:
            earning = Decimal("0")
            if trade["sold"]:
                earning += (
                    Decimal(trade["sold"])
                    * Decimal(trade["matecoin_price"])
                )
                profit["matecoin_account"] -= Decimal(trade["sold"])
            if trade["bought"]:
                earning -= (
                    Decimal(trade["bought"])
                    * Decimal(trade["matecoin_price"])
                )
                profit["matecoin_account"] += Decimal(trade["bought"])
            profit["earned_money"] += earning
    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
