import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data = json.load(file)

    sold = decimal.Decimal("0.0")
    bought = decimal.Decimal("0.0")
    amount_sold = decimal.Decimal("0.0")
    amount_bought = decimal.Decimal("0.0")

    for item in data:
        if item["bought"]:
            temp_bought = decimal.Decimal(item["bought"])
            temp_mate_price = decimal.Decimal(item["matecoin_price"])
            bought += temp_bought * temp_mate_price
            amount_bought += temp_bought
        if item["sold"]:
            temp_sold = decimal.Decimal(item["sold"])
            temp_mate_price = decimal.Decimal(item["matecoin_price"])
            sold += temp_sold * temp_mate_price
            amount_sold += temp_sold

    earned_money = sold - bought
    matecoin_account = amount_bought - amount_sold

    final_result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(final_result, file, indent=2)
