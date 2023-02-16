import json
import decimal


def calculate_profit(file_name: str) -> None:
    result = {
        "earned_money": decimal.Decimal("0"),
        "matecoin_account": decimal.Decimal("0")
    }
    with open(file_name, "r") as file_input:
        data = json.load(file_input)

    for raw in data:

        if raw.get("bought"):
            bought = decimal.Decimal(raw.get("bought"))
            matecoin_price = decimal.Decimal(raw.get("matecoin_price"))
            result["earned_money"] -= bought * matecoin_price
            result["matecoin_account"] += bought

        if raw.get("sold"):
            sold = decimal.Decimal(raw.get("sold"))
            matecoin_price = decimal.Decimal(raw.get("matecoin_price"))
            result["earned_money"] += sold * matecoin_price
            result["matecoin_account"] -= sold

    result["earned_money"] = str(result["earned_money"])
    result["matecoin_account"] = str(result["matecoin_account"])

    with open("profit.json", "w") as file_output:
        json.dump(result, file_output, indent=2)
