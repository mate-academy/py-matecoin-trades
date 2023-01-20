# write your code here
from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as js_file:
        trades = json.load(js_file)
    money = 0
    account = 0
    for trade in trades:
        if trade["bought"] is not None:
            account += Decimal(trade["bought"])
            money -= (Decimal(trade["bought"])
                      * Decimal(trade["matecoin_price"]))
        if trade["sold"] is not None:
            account -= Decimal(trade["sold"])
            money += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
    with open("profit.json", "w") as js_profit:
        json.dump(
            {
                "earned_money": str(money),
                "matecoin_account": str(account)
            },
            js_profit, indent=2
        )