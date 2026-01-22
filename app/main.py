import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought_volume = (
            Decimal(trade["bought"])) \
            if trade["bought"] \
            else Decimal("0")
        sold_volume = (
            Decimal(trade["sold"])) \
            if trade["sold"] \
            else Decimal("0")
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought_volume:
            matecoin_account += bought_volume
            earned_money -= bought_volume * matecoin_price

        if sold_volume:
            matecoin_account -= sold_volume
            earned_money += sold_volume * matecoin_price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    path = Path(__file__).resolve().parent.parent / "profit.json"
    with open(path, "w") as outfile:
        json.dump(result, outfile, indent=2)
