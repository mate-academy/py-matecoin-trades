# write your code here
import json
from decimal import Decimal


def calculate_profit(filename: str = "trades.json") -> None:
    with open(filename, "r") as file_in:
        trade_list = json.load(file_in)

        money_profit = 0
        mate_coin_account = 0
        for trade in trade_list:
            if trade["bought"] is not None:
                mate_coin_account += Decimal(trade["bought"])
                money_profit -= Decimal(trade["bought"]) * \
                    Decimal(trade["matecoin_price"])

            if trade["sold"] is not None:
                mate_coin_account -= Decimal(trade["sold"])
                money_profit += Decimal(trade["sold"]) * \
                    Decimal(trade["matecoin_price"])

        profit = {
            "earned_money": str(money_profit),
            "matecoin_account": str(mate_coin_account)
        }
        with open("profit.json", "w") as file_out:
            json.dump(profit, file_out, indent=2)
