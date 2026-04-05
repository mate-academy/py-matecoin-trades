import decimal
import json


def calculate_profit(file_data) -> None:
    with open(file_data, "r") as file:
        data = json.load(file)
        earned_money = decimal.Decimal("0")
        matecoin_account = decimal.Decimal("0")
        for item in data:
            if item["bought"] is not None:
                bought_amount = decimal.Decimal(item["bought"])
                price = decimal.Decimal(item["matecoin_price"])

                matecoin_account += bought_amount
                earned_money -= bought_amount * price

            if item["sold"] is not None:
                sold_amount = decimal.Decimal(item["sold"])
                price = decimal.Decimal(item["matecoin_price"])

                matecoin_account -= sold_amount
                earned_money += sold_amount * price
    final_result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(final_result, file, indent=2)
