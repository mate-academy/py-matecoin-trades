import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        trades = json.load(json_file)
        profit_dict = dict()

        for trade in trades:
            if trade["bought"]:

                profit_dict["earned_money"] = \
                    profit_dict.get("earned_money", 0) - \
                    Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])

                profit_dict["matecoin_account"] = \
                    profit_dict.get("matecoin_account", 0) + \
                    Decimal(trade["bought"])

            if trade["sold"]:

                profit_dict["earned_money"] = \
                    profit_dict.get("earned_money", 0) + \
                    Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])

                profit_dict["matecoin_account"] = \
                    profit_dict.get("matecoin_account", 0) - \
                    Decimal(trade["sold"])

        for key, value in profit_dict.items():
            profit_dict[key] = str(value)

        with open("profit.json", "w") as profit_file:
            json.dump(profit_dict, profit_file, indent=2)
