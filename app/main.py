import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        trades_information = json.load(f)
        account, earned = 0, 0

        for trade in trades_information:
            if trade["bought"]:
                account += Decimal(trade["bought"])
                earned -= Decimal(trade["bought"]) \
                    * Decimal(trade["matecoin_price"])

            if trade["sold"]:
                account -= Decimal(trade["sold"])
                earned += Decimal(trade["sold"]) \
                    * Decimal(trade["matecoin_price"])

        profit = {
            "earned_money": str(earned),
            "matecoin_account": str(account)
        }

    with open("profit.json", "w") as new_file:
        json.dump(profit, new_file, indent=2)
