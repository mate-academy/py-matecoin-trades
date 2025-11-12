from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data = json.load(file)
        result = {
            "earned_money": "0",
            "matecoin_account": "0"
        }

        earned_money = Decimal("0")
        spent_money = Decimal("0")
        count_matecoin = Decimal("0")

        for item in data:
            price = Decimal(item.get("matecoin_price"))
            if item.get("bought") is not None:
                bought = Decimal(item["bought"])
                spent_money += bought * price
                count_matecoin += bought
            if item.get("sold") is not None:
                sold = Decimal(item["sold"])
                earned_money += sold * price
                count_matecoin -= sold

        profit = earned_money - spent_money

        result["earned_money"] = str(profit)
        result["matecoin_account"] = str(count_matecoin)

    with open("profit.json", "w") as out_file:
        json.dump(result, out_file)
