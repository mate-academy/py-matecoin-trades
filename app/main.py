import json
import decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades_list = json.load(file)
        earned_money = decimal.Decimal("0")
        matecoin_account = decimal.Decimal("0")

        for trade in trades_list:
            if trade["bought"] is not None:
                matecoin_account += decimal.Decimal(trade["bought"])
                earned_money -= (
                    decimal.Decimal(trade["bought"])
                    * decimal.Decimal(trade["matecoin_price"])
                )

            if trade["sold"] is not None:
                matecoin_account -= decimal.Decimal(trade["sold"])
                earned_money += (
                    decimal.Decimal(trade["sold"])
                    * decimal.Decimal(trade["matecoin_price"])
                )

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }
        with open("profit.json", "w") as f:
            json.dump(result, f, indent=2)
