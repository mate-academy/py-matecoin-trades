import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        all_trades = json.load(f)

        earned_money = decimal.Decimal("0.0")
        matecoin_account = decimal.Decimal("0.0")

        for trade in all_trades:
            if trade["bought"] is not None:
                earned_money -= decimal.Decimal(
                    trade["bought"]) * decimal.Decimal(
                    trade["matecoin_price"]
                )
                matecoin_account += decimal.Decimal(trade["bought"])

            if trade["sold"] is not None:
                earned_money += decimal.Decimal(
                    trade["sold"]) * decimal.Decimal(
                    trade["matecoin_price"]
                )
                matecoin_account -= decimal.Decimal(trade["sold"])

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
