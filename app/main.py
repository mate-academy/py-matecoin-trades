import json
from decimal import Decimal


def calculate_profit(file_js_objects: str) -> None:
    profit = Decimal("0")
    current_coin_account = Decimal("0")
    value_current_coin_account = Decimal("0")
    with open(file_js_objects, "r") as read_file:
        trades_information = json.load(read_file)
        for trade in trades_information:
            if trade["bought"]:
                current_coin_account += Decimal(trade["bought"])
                value_current_coin_account += (
                    Decimal(trade["bought"])
                    * Decimal(trade["matecoin_price"])
                )
            if trade["sold"]:
                profit = (
                    Decimal(trade["matecoin_price"])
                    * Decimal(trade["sold"])
                    - value_current_coin_account
                )
                current_coin_account -= Decimal(trade["sold"])
                value_current_coin_account -= (
                    Decimal(trade["sold"])
                    * Decimal(trade["matecoin_price"])
                )
    profit_string = {
        "earned_money": str(profit),
        "matecoin_account": str(current_coin_account)
    }

    with open("profit.json", "w") as write_file:
        json.dump(profit_string, write_file, indent=2)
