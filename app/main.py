from decimal import Decimal
import json


def calculate_profit(trades: str) -> None:
    with (
        open(trades, "r") as file_in,
        open("profit.json", "w") as file_out
    ):
        matecoin_data = json.load(file_in)
        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for data in matecoin_data:
            if data["bought"] is not None:
                earned_money -= (
                    Decimal(data["bought"])
                    * Decimal(data["matecoin_price"])
                )
                matecoin_account += Decimal(data["bought"])
            if data["sold"] is not None:
                earned_money += (
                    Decimal(data["sold"])
                    * Decimal(data["matecoin_price"])
                )
                matecoin_account -= Decimal(data["sold"])

        profit_data = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        json.dump(profit_data, file_out, indent=2)

