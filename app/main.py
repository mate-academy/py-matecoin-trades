import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as tr:
        trades_data = json.load(tr)

    result_dict = {
        "earned_money": "0.0",
        "matecoin_account": "0.0"
    }
    for i in trades_data:
        if isinstance(i.get("bought"), str):

            result_dict["earned_money"] = str(Decimal(result_dict.get(
                "earned_money")) - (
                Decimal(i.get("bought")) * Decimal(i.get("matecoin_price"))
            ))

            result_dict["matecoin_account"] = str(Decimal(result_dict.get(
                "matecoin_account")) + Decimal(i.get("bought")))
        if isinstance(i.get("sold"), str):
            result_dict["earned_money"] = str(Decimal(result_dict.get(
                "earned_money")) + (
                Decimal(i.get("sold")) * Decimal(i.get("matecoin_price"))
            ))

            result_dict["matecoin_account"] = str(Decimal(result_dict.get(
                "matecoin_account")) - Decimal(i.get("sold")))

    with open("profit.json", "w") as file:
        json.dump(result_dict, file, indent=2)
