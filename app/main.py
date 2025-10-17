import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as trades_file:
        trades = json.load(trades_file)
        matecoin_account = Decimal("0.0")
        earned_money = Decimal("0.0")
        for trade in trades:
            if "bought" in trade:
                if trade["bought"] is None:
                    bought = Decimal("0.0")
                else:
                    bought = Decimal(trade["bought"])
                price = Decimal(trade["matecoin_price"])
                matecoin_account += bought
                earned_money -= bought * price
            if "sold" in trade:
                if trade["sold"] is None:
                    sold = Decimal("0.0")
                else:
                    sold = Decimal(trade["sold"])
                price = Decimal(trade["matecoin_price"])
                matecoin_account -= sold
                earned_money += sold * price

        profit_dict = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }
        with open("profit.json", "w") as profit_file:
            json.dump(profit_dict, profit_file, indent=2)
