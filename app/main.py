import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name) as input_file:
        json_data = json.load(input_file)

    zero = decimal.Decimal("0")
    earnings = {"earned_money": zero, "matecoin_account": zero}
    for day in json_data:
        matecoin_price = decimal.Decimal(day["matecoin_price"])
        sold = decimal.Decimal(day["sold"]) if day["sold"] else zero
        bought = decimal.Decimal(day["bought"]) if day["bought"] else zero
        earnings["earned_money"] += matecoin_price * (sold - bought)
        earnings["matecoin_account"] += bought - sold
    earnings = {key: str(value) for key, value in earnings.items()}

    with open("profit.json", "w") as output_file:
        json.dump(earnings, output_file, indent=2)
