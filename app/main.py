import json
from decimal import Decimal


def calculate_profit(filename: str) -> Decimal:
    with open(filename, "r") as file:
        trades = json.load(file)

    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    for trade in trades:
        price_val = trade.get("matecoin_price")
        if price_val is None:
            continue

        price = Decimal(str(price_val))

        if (bought := trade.get("bought")) is not None:
            amount = Decimal(str(bought))
            matecoin_account += amount
            earned_money -= amount * price

        if (sold := trade.get("sold")) is not None:
            amount = Decimal(str(sold))
            matecoin_account -= amount
            earned_money += amount * price

    result = {
        "matecoin_account": str(matecoin_account),
        "earned_money": str(earned_money)
    }

    with open("profit.json", "w") as outfile:
        json.dump(result, outfile, indent=4)


if __name__ == "__main__":
    calculate_profit("trades.json")
