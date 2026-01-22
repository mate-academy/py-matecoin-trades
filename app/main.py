import decimal
import json


def calculate_profit(trades_json: str) -> None:
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    with open(trades_json, "r") as trades_file:
        trades_data = json.load(trades_file)

        for operation in trades_data:
            if isinstance(operation["bought"], str):
                earned_money -= (
                    decimal.Decimal(operation["bought"])
                    * decimal.Decimal(operation["matecoin_price"])
                )
                matecoin_account += decimal.Decimal(operation["bought"])

            if isinstance(operation["sold"], str):
                earned_money += (
                    decimal.Decimal(operation["sold"])
                    * decimal.Decimal(operation["matecoin_price"])
                )
                matecoin_account -= decimal.Decimal(operation["sold"])

    with open("profit.json", "w") as profit:
        profit_dict = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        json.dump(profit_dict, profit, indent=2)
