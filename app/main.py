import json
import decimal


def calculate_profit(json_file: str) -> None:
    with open(json_file, "r") as file:
        data_array = json.load(file)
    profit = decimal.Decimal("0.0")
    checks = decimal.Decimal("0.0")
    for data in data_array:
        if data.get("bought"):
            profit -= (decimal.Decimal(data.get("bought"))
                       * decimal.Decimal(data.get("matecoin_price")))
            checks += decimal.Decimal(data.get("bought"))
        if data.get("sold"):
            profit += (decimal.Decimal(data.get("sold"))
                       * decimal.Decimal(data.get("matecoin_price")))
            checks -= decimal.Decimal(data.get("sold"))

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(checks),
    }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
