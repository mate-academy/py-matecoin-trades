import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for transaction in data:
        price = Decimal(transaction["matecoin_price"])
        bought = transaction["bought"]
        sold = transaction["sold"]
        if bought is not None:
            matecoin_account += Decimal(bought)
            earned_money -= Decimal(bought) * Decimal(price)

        if sold is not None:
            matecoin_account -= Decimal(sold)
            earned_money += Decimal(sold) * Decimal(price)
    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as result_file:
        json.dump(profit_data, result_file, indent=2)
