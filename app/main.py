import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file_in:
        trades = json.load(file_in)

        bought = Decimal(0)
        sold = Decimal(0)
        bought_amount_coin = Decimal(0)
        sold_amount_coin = Decimal(0)

        for trade in trades:
            if trade["bought"] is not None:
                bought_amount_coin += Decimal(trade["bought"])
                bought -= (Decimal(trade["bought"])
                           * Decimal(trade["matecoin_price"]))

            if trade["sold"] is not None:
                sold_amount_coin += Decimal(trade["sold"])
                sold -= (Decimal(trade["sold"])
                         * Decimal(trade["matecoin_price"]))

        matecoin_account_amount = bought_amount_coin - sold_amount_coin
        profit_amount = bought - sold

        profit = {
            "earned_money": str(profit_amount),
            "matecoin_account": str(matecoin_account_amount)
        }

        with open("profit.json", "w") as file_out:
            json.dump(profit, file_out, indent=2)
