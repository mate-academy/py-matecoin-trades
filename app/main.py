import json
import decimal


def calculate_profit(file_name: str) -> dict[str, str] | None:
    with open(file_name, "r") as file:
        trades = json.load(file)

        profits = {
            "earned_money": decimal.Decimal("0"),
            "matecoin_account": decimal.Decimal("0")
        }
        for trade in trades:
            bought = decimal.Decimal(
                trade["bought"]
            ) if trade["bought"] else decimal.Decimal("0")
            sold = decimal.Decimal(
                trade["sold"]
            ) if trade["sold"] else decimal.Decimal("0")
            price = decimal.Decimal(trade["matecoin_price"])
            profits["matecoin_account"] += bought - sold
            profits["earned_money"] += (sold - bought) * price

        result = {
            "earned_money": str(profits["earned_money"]),
            "matecoin_account": str(profits["matecoin_account"])
        }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
