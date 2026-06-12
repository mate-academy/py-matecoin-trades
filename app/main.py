import json
from decimal import Decimal


# write your code here
def calculate_profit(json_file_name: str) -> None:
    with open(json_file_name, "r") as file:
        trades = json.load(file)
        matecoin_account = Decimal("0")
        earned_money = Decimal("0")
        i = 0
        while i < len(trades):
            coin_price = Decimal(trades[i]["matecoin_price"])
            if trades[i]["bought"] is not None:
                earned_money -= Decimal(trades[i]["bought"]) * coin_price
                matecoin_account = (
                    Decimal(matecoin_account) + Decimal(trades[i]["bought"])
                )
            if trades[i]["sold"] is not None:
                earned_money += Decimal(trades[i]["sold"]) * coin_price
                matecoin_account = (
                    Decimal(matecoin_account) - Decimal(trades[i]["sold"])
                )
            i += 1

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as profit_file:
            json.dump(result, profit_file, indent=2)
