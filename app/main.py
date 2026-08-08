import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        metacoin_trades = json.load(f)
    earned_money = 0
    matecoin_account = 0

    for trade in metacoin_trades:
        if trade["bought"] is not None:
            earned_money -= (decimal.Decimal(trade["matecoin_price"])
                             * decimal.Decimal(trade["bought"]))
            matecoin_account += decimal.Decimal(trade["bought"])
        if trade["sold"] is not None:
            earned_money += (decimal.Decimal(trade["matecoin_price"])
                             * decimal.Decimal(trade["sold"]))
            matecoin_account -= decimal.Decimal(trade["sold"])

    metacoin_profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as n:
        json.dump(metacoin_profit, n, indent=2)
