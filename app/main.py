import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    try:
        with open(file_path, "r") as trades:
            data = json.load(trades)
            bought_coins = []
            sold_coins = []
            account = 0
            profit_dict = {}
            for trade in data:
                if trade["bought"] and trade["bought"] != "None":
                    bought = Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
                    bought_coins.append(bought)
                    account += Decimal(trade["bought"])
                if trade["sold"] and trade["bought"] != "None":
                    sold = Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
                    sold_coins.append(sold)
                    account -= Decimal(trade["sold"])

            earned_money = sum(sold_coins) - sum(bought_coins)

            profit_dict["earned_money"] = str(earned_money)
            profit_dict["matecoin_account"] = str(account)

            with open("profit.json", "w") as profit:
                json.dump(profit_dict, profit, indent=2)
    except Exception as e:
        print("Error:", e)
