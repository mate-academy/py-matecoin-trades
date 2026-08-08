import json
from decimal import Decimal


def calculate_profit(trades_json: str) -> None:
    with open(trades_json, "r") as trades:
        trade_journal = json.load(trades)
        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for char in trade_journal:
            price = Decimal(char["matecoin_price"])
            if char["bought"]:
                bought = Decimal(char["bought"])
                earned_money -= bought * price
                matecoin_account += bought
            if char["sold"]:
                sold = Decimal(char["sold"])
                earned_money += sold * price
                matecoin_account -= sold

        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as profits_journal:
            json.dump(profit, profits_journal, indent=2)
