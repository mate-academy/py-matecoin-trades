from decimal import Decimal
import json


def calculate_profit(trades: json) -> None:
    with open(trades) as source_json:
        data = json.load(source_json)
        earned_money = Decimal("0")
        matecoin_account = Decimal("0")
        for field in data:
            if field["bought"] is not None:
                matecoin_account += (Decimal(field["bought"]))
                earned_money -= Decimal(field["bought"]) * \
                    Decimal(field["matecoin_price"])
            if field["sold"] is not None:
                matecoin_account -= (Decimal(field["sold"]))
                earned_money += Decimal(field["sold"]) * \
                    Decimal(field["matecoin_price"])
        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        with open("profit.json", "w") as result_json:
            json.dump(profit, result_json, indent=2)
