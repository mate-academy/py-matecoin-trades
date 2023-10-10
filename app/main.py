import json
from decimal import Decimal


def calculate_profit(
        input_filename: str,
        output_filename: str
) -> None:
    with open(input_filename, "r") as input_file:
        trades = json.load(input_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade.get("bought"))
        sold = Decimal(trade.get("sold"))
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought > 0:
            earned_money -= bought * matecoin_price
            matecoin_account += bought
        elif sold > 0:
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(output_filename, "w") as output_file:
        json.dump(result, output_file, indent=2)
