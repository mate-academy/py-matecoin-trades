import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trade = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for operation in trade:
        price = Decimal(operation["matecoin_price"])
        bought = operation["bought"]
        sold = operation["sold"]
        if bought is not None:
            matecoin_account += Decimal(bought)
            earned_money -= Decimal(bought) * Decimal(price)

        if sold is not None:
            matecoin_account -= Decimal(sold)
            earned_money += Decimal(sold) * Decimal(price)
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
