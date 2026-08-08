import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)

    profit = decimal.Decimal("0")
    mate_coin = decimal.Decimal("0")

    for day in data:
        price = decimal.Decimal(str(day.get("matecoin_price")))
        if day.get("bought"):
            bought = decimal.Decimal(str(day["bought"]))
            mate_coin += bought
            profit -= bought * price
        if day.get("sold"):
            sold = decimal.Decimal(str(day["sold"]))
            mate_coin -= sold
            profit += sold * price

    result_dict = {
        "earned_money": str(profit),
        "matecoin_account": str(mate_coin)
    }

    with open("profit.json", "w") as profit_json_file:
        json.dump(result_dict, profit_json_file, indent=2)
