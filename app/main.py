import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with (open(file_name, "r") as trades_file,
          open("profit.json", "w") as profit_file):

        trades_list = json.load(trades_file)
        matecoin_account = Decimal(0)
        earned_money = Decimal(0)

        for trade in trades_list:
            if trade.get("bought"):
                bought_amount = Decimal(trade["bought"])
                matecoin_account += bought_amount
                earned_money -= (bought_amount
                                 * Decimal(trade["matecoin_price"]))
            if trade.get("sold"):
                sold_amount = Decimal(trade["sold"])
                matecoin_account -= sold_amount
                earned_money += sold_amount * Decimal(trade["matecoin_price"])

        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            profit_file,
            indent=2
        )
