import json
import decimal


def calculate_profit(name_file: str) -> None:
    with (open(name_file, "r") as file):
        data = json.load(file)
        money = {
            "earned_money": decimal.Decimal("0.0"),
            "matecoin_account": decimal.Decimal("0.0")
        }
        for item in data:
            price = decimal.Decimal(item["matecoin_price"])

            if item["bought"] is not None:
                bought = decimal.Decimal(item["bought"])
                money["earned_money"] -= bought * price
                money["matecoin_account"] += bought

            if item["sold"] is not None:
                sold = decimal.Decimal(item["sold"])
                money["earned_money"] += sold * price
                money["matecoin_account"] -= sold

    with open("profit.json", "w") as file:
        money["earned_money"] = str(money["earned_money"])
        money["matecoin_account"] = str(money["matecoin_account"])
        json.dump(money, file, indent=2)
