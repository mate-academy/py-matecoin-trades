import decimal
import json


def calculate_profit() -> None:
    with open("trades.json") as file:
        trades_data = json.load(file)

    matecoin = decimal.Decimal("0")
    earned_money = decimal.Decimal("0")

    for day in trades_data:
        if day["bought"] is not None:
            matecoin += decimal.Decimal(day["bought"])
            earned_money -= (
                decimal.Decimal(day["matecoin_price"])
                * decimal.Decimal(day["bought"])
            )
        if day["sold"] is not None:
            matecoin -= decimal.Decimal(day["sold"])
            earned_money += (
                decimal.Decimal(day["matecoin_price"])
                * decimal.Decimal(day["sold"])
            )

    profit = [{
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin)
    }]

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
