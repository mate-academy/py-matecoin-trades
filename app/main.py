from decimal import Decimal
import json


def calculate_profit(trade_file_path: str) -> None:
    with (open(trade_file_path, "r") as file):
        trades = json.load(file)
        profit = 0
        account = 0
        for trade in trades:
            if "bought" in trade and trade["bought"]:
                profit -= (Decimal(trade["bought"])
                           * Decimal(trade["matecoin_price"]))
                account += Decimal(trade["bought"])
            if "sold" in trade and trade["sold"]:
                profit += (Decimal(trade["sold"])
                           * Decimal(trade["matecoin_price"]))
                account -= Decimal(trade["sold"])
        profit_data = {
            "earned_money": str(profit),
            "matecoin_account": str(account)
        }
        with open("profit.json", "w") as result_file:
            json.dump(profit_data, result_file, indent=2)
