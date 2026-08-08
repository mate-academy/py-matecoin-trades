import json
import decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as f:
        trades = json.load(f)

    earned_money = decimal.Decimal("0.00000")
    matecoin_account = decimal.Decimal("0.00000")

    for trade in trades:
        bought = trade["bought"]
        sold = trade["sold"]
        matecoin_price = decimal.Decimal(trade["matecoin_price"])

        if bought is not None:
            matecoin_account += decimal.Decimal(bought)
            earned_money -= decimal.Decimal(bought) * matecoin_price
        if sold is not None:
            matecoin_account -= decimal.Decimal(sold)
            earned_money += decimal.Decimal(sold) * matecoin_price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
