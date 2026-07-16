import json
import pathlib
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = trade["bought"]
        sold = trade["sold"]
        matecoin_price = trade["matecoin_price"]

        matecoin_price_decimal = Decimal(matecoin_price)

        if bought is not None:
            bought_decimal = Decimal(bought)
            earned_money -= bought_decimal * matecoin_price_decimal
            matecoin_account += bought_decimal

        if sold is not None:
            sold_decimal = Decimal(sold)
            earned_money += sold_decimal * matecoin_price_decimal
            matecoin_account -= sold_decimal

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(
            pathlib.Path(__file__).resolve().parent.parent / "profit.json", "w"
    ) as file:
        json.dump(result, file, indent=2)
