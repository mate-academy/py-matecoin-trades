import json
from decimal import Decimal


def calculate_profit(source_file: str) -> None:
    with open(source_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for operation in trades:
        raw_bought = operation["bought"]
        raw_sold = operation["sold"]

        bought = (
            Decimal(raw_bought)) \
            if raw_bought is not None \
            else Decimal("0")

        sold = Decimal(raw_sold) if raw_sold is not None else Decimal("0")
        matecoin_price = Decimal(operation["matecoin_price"])

        earned_money += (sold * matecoin_price) - (bought * matecoin_price)
        matecoin_account += bought - sold

    with open("profit.json", "w") as file:
        json.dump(
            {"earned_money": str(earned_money),
             "matecoin_account": str(matecoin_account)},
            file,
            indent=2
        )
