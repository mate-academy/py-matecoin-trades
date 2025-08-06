import json
import os
from decimal import Decimal


def calculate_profit(trade_file: str) -> None:
    if trade_file is None:
        trade_file = os.path.join(os.path.dirname(__file__), "trades.json")
    with (open(trade_file, "r") as file):
        trades = json.load(file)
        money_profit = Decimal("0")
        current_account = Decimal("0")

        for oper in trades:
            bought = (
                Decimal(str(oper["bought"]))
                if oper["bought"] is not None else Decimal("0")
            )
            sold = (
                Decimal(str(oper["sold"]))
                if oper["sold"] is not None else Decimal("0")
            )
            price = Decimal(str(oper["matecoin_price"]))
            money_profit += sold * price - bought * price
            current_account += (bought - sold)
        profit = {
            "earned_money": f"{money_profit}",
            "matecoin_account": f"{current_account}"
        }
        with open("profit.json", "w") as file:
            json.dump(profit, file, indent=2)
