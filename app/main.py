import decimal
import json
import os


def calculate_profit(file_name: str) -> None:
    if not os.path.isabs(file_name):
        file_name = os.path.join("app", file_name)

    results = {
        "earned_money": decimal.Decimal(0),
        "matecoin_account": decimal.Decimal(0)
    }

    with (open(file_name, "r") as trade_data,
          open("profit.json", "w") as profit):
        trade_data = json.load(trade_data)

        for day in trade_data:
            bought = decimal.Decimal(
                day["bought"]
            ) if day["bought"] else decimal.Decimal(0)
            sold = decimal.Decimal(
                day["sold"]
            ) if day["sold"] else decimal.Decimal(0)
            price = decimal.Decimal(
                day["matecoin_price"]
            )

            if sold:
                results["earned_money"] += sold * price
                results["matecoin_account"] -= sold
            if bought:
                results["earned_money"] -= bought * price
                results["matecoin_account"] += bought

        json.dump(
            {param: str(value) for param, value in results.items()}, profit,
            indent=2
        )
