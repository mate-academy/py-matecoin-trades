import json

import decimal

def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        transaction_data = json.load(file)

    matecoin_account = decimal.Decimal("0.0")
    bought_total = decimal.Decimal("0.0")
    sold_total = decimal.Decimal("0.0")

    for data in transaction_data:
        if data["bought"]:
            matecoin_account += decimal.Decimal(data["bought"])
            bought_total += decimal.Decimal(data["bought"]) * decimal.Decimal(data["matecoin_price"])
        if data["sold"]:
            matecoin_account -= decimal.Decimal(data["sold"])
            sold_total += decimal.Decimal(data["sold"]) * decimal.Decimal(data["matecoin_price"])

    with open("profit.json", "w") as profit_file:
        json.dump({"earned_money": str(sold_total - bought_total), "matecoin_account": str(matecoin_account)},
                  profit_file, indent=2)
