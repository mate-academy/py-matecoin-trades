import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        data = json.load(f)

    result = {"earned_money": Decimal(0), "matecoin_account": Decimal(0)}

    total_spent = Decimal("0")
    total_earned = Decimal("0")

    for data_dict in data:
        if bought := data_dict.get("bought"):
            result["matecoin_account"] = (
                Decimal(result.get("matecoin_account")) + Decimal(bought)
            )
            total_spent += (
                Decimal(bought) * Decimal(data_dict.get("matecoin_price"))
            )

        if sold := data_dict.get("sold"):
            result["matecoin_account"] = (
                Decimal(result.get("matecoin_account")) - Decimal(sold)
            )
            total_earned += (
                Decimal(sold) * Decimal(data_dict.get("matecoin_price"))
            )

        result["earned_money"] = total_earned - total_spent

    for key, value in result.items():
        result.update({key: str(value)})

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
