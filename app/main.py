from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(str(file_name), "r") as f, open("profit.json", "a") as r:
        data = json.load(f)

        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for action in data:
            if action["bought"] is not None:
                matecoin_account += Decimal(action["bought"])
                costs = Decimal(action["bought"])\
                    * Decimal(action["matecoin_price"])
                earned_money -= costs

            if action["sold"] is not None:
                matecoin_account -= Decimal(action["sold"])
                costs = Decimal(action["sold"])\
                    * Decimal(action["matecoin_price"])
                earned_money += costs

        output = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        json.dump(output, r, indent=2)
