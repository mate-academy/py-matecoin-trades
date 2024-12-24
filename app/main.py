import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file, open("profit.json", "w") as profit_json:
        data_coin = json.load(file)
        earned_money = Decimal("0.0")
        matecoin_account = Decimal("0.0")

        for transaction in data_coin:
            if transaction["bought"] is not None:
                earned_money -= (
                        Decimal(str(transaction["bought"])) *
                        Decimal(str(transaction["matecoin_price"]))
                )
                matecoin_account += Decimal(str(transaction["bought"]))
            if transaction["sold"] is not None:
                earned_money += (
                        Decimal(str(transaction["sold"])) * 
                        Decimal(str(transaction["matecoin_price"]))
                )
                matecoin_account -= Decimal(str(transaction["sold"]))

        profit_to_js = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(profit_to_js, profit_json, indent=2)
