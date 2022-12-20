from decimal import Decimal
import json


def calculate_profit(trades: json) -> None:
    result_transaction_string = {"earned_money": 0, "matecoin_account": 0}
    with open(trades, "r") as read_file:
        trades_info = json.load(read_file)

        for transaction in trades_info:
            if transaction["bought"] is not None:
                result_transaction_string["earned_money"] -= (
                    Decimal(transaction["bought"])
                    * Decimal(transaction["matecoin_price"])
                )

                result_transaction_string["matecoin_account"] += Decimal(
                    transaction["bought"]
                )

            if transaction["sold"] is not None:
                result_transaction_string["earned_money"] += (Decimal(
                    transaction["sold"]
                ) * Decimal(transaction["matecoin_price"]))
                result_transaction_string["matecoin_account"] -= Decimal(
                    transaction["sold"]
                )

    for key, value in result_transaction_string.items():
        result_transaction_string[key] = str(value)

    with open("profit.json", "w") as result_file:
        json.dump(result_transaction_string, result_file, indent=2)
