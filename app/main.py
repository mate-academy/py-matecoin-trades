from decimal import Decimal
import json


def calculate_profit(file_name: str = "trades.json") -> None:
    with open(file_name) as file:
        input_data = json.load(file)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for item in input_data:
        if item["bought"] is not None:
            bought_amount = Decimal(item["bought"])
            matecoin_price_amount = Decimal(item["matecoin_price"])
            earned_money -= bought_amount * matecoin_price_amount
            matecoin_account += bought_amount
        if item["sold"] is not None:
            matecoin_price_amount = Decimal(item["matecoin_price"])
            sold_amount = Decimal(item["sold"])
            earned_money += sold_amount * matecoin_price_amount
            matecoin_account -= sold_amount

    output_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file_out:
        json.dump(output_data, file_out, indent=2)
