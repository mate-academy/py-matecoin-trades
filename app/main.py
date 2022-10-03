import json
from decimal import Decimal


def calculate_profit(file_name: str):
    with open(file_name) as source, open("profit.json", "w") as target:
        dictionaries = json.load(source)
        result = {
            "purchase costs": Decimal("0.0"),
            "sales revenue": Decimal("0.0"),
            "couins amount": Decimal("0")
        }

        for dictionary in dictionaries:
            if dictionary["bought"] is not None:
                result["purchase costs"] += Decimal(dictionary["bought"]) * \
                    Decimal(dictionary["matecoin_price"])
                result["couins amount"] += Decimal(dictionary["bought"])
            if dictionary["sold"] is not None:
                result["sales revenue"] += Decimal(dictionary["sold"]) * \
                    Decimal(dictionary["matecoin_price"])
                result["couins amount"] -= Decimal(dictionary["sold"])

        profit = {
            "earned_money": str(
                result["sales revenue"] - result["purchase costs"]
            ),
            "matecoin_account": str(result["couins amount"])
        }
        json.dump(profit, target, indent=2)
