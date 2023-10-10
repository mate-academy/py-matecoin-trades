import json
from decimal import Decimal


def calculate_profit(operation_file: json) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(operation_file) as file:
        currency_data = json.load(file)
        for date in currency_data:
            bought = date.get("bought")
            sold = date.get("sold")
            matecoin_price = Decimal(date["matecoin_price"])
            if bought:
                bought = Decimal(bought)
                earned_money -= bought * matecoin_price
                matecoin_account += bought
            if sold:
                sold = Decimal(sold)
                earned_money += sold * matecoin_price
                matecoin_account -= sold
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
