import json
from decimal import Decimal


def calculate_profit(
        trades_file: str,
        output_file: str = "profit.json"
) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trades:
        if trade["bought"] is not None:
            bought_volume = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            cost = bought_volume * matecoin_price
            earned_money -= cost
            matecoin_account += bought_volume

        if trade["sold"] is not None:
            sold_volume = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            revenue = sold_volume * matecoin_price
            earned_money += revenue
            matecoin_account -= sold_volume

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(output_file, "w") as output_file:
        json.dump(result, output_file, indent=2)
