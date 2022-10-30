from decimal import Decimal
import json


def calculate_profit(trades: str) -> None:
    earned, account = 0, 0

    with open(trades) as file_in, open("profit.json", "w") as file_out:
        data_trades = json.load(file_in)

        for trade in data_trades:

            if trade["sold"]:
                account -= Decimal(trade["sold"])
                earned += Decimal(trade["sold"]) \
                    * Decimal(trade["matecoin_price"])

            if trade["bought"]:
                account += Decimal(trade["bought"])
                earned -= Decimal(trade["bought"]) \
                    * Decimal(trade["matecoin_price"])

        profit = {
            "earned_money": str(earned),
            "matecoin_account": str(account)
        }

        json.dump(profit, file_out, indent=2)
