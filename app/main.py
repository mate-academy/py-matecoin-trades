import json
import decimal


def calculate_profit(trades_file: str) -> None:
    total = {"earned_money": "0", "matecoin_account": "0"}
    with open(trades_file) as file_out:
        transactions = json.load(file_out)
        for transaction in transactions:
            transaction["bought"] = (
                "0" if transaction["bought"] is None else transaction["bought"]
            )
            transaction["sold"] = (
                "0" if transaction["sold"] is None else transaction["sold"]
            )
            total["earned_money"] = str(
                decimal.Decimal(total["earned_money"])
                - (
                    decimal.Decimal(transaction["bought"])
                    - decimal.Decimal(transaction["sold"])
                )
                * decimal.Decimal(transaction["matecoin_price"])
            )
            total["matecoin_account"] = str(
                decimal.Decimal(total["matecoin_account"])
                + (
                    decimal.Decimal(transaction["bought"])
                    - decimal.Decimal(transaction["sold"])
                )
            )

        with open("profit.json", "w") as file_in:
            json.dump(total, file_in, indent=2)
