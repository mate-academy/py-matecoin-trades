import json
from decimal import Decimal, ROUND_DOWN


def calculate_profit(trades_file: json) -> None:
    with open(trades_file, "r") as f:
        trades_data = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        bought = Decimal(trade["bought"]) if trade["bought"] else None
        sold = Decimal(trade["sold"]) if trade["sold"] else None
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought is not None:
            matecoin_account += bought
            earned_money -= bought * matecoin_price
        if sold is not None:
            matecoin_account -= sold
            earned_money += sold * matecoin_price

    earned_money = earned_money.quantize(Decimal("0.0000000"),
                                         rounding=ROUND_DOWN)
    matecoin_account = matecoin_account.quantize(Decimal("0.00000"),
                                                 rounding=ROUND_DOWN)

    with open("profit.json", "w") as profit_json:
        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        json.dump(result, profit_json, indent=2)
