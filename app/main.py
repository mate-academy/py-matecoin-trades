import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data = json.load(file)
    result = {
        "earned_money": decimal.Decimal("0"),
        "matecoin_account": decimal.Decimal("0")
    }
    for dct in data:
        if dct["bought"] is not None:
            result["earned_money"] -= (
                decimal.Decimal(dct["bought"])
                * decimal.Decimal(dct["matecoin_price"])
            )
            result["matecoin_account"] += decimal.Decimal(dct["bought"])
        if dct["sold"] is not None:
            result["earned_money"] += (
                decimal.Decimal(dct["sold"])
                * decimal.Decimal(dct["matecoin_price"])
            )
            result["matecoin_account"] -= decimal.Decimal(dct["sold"])
    result = {key: str(value) for key, value in result.items()}
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
