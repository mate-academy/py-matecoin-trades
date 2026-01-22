import json

from decimal import Decimal


def calculate_profit(data_file_name: str) -> None:
    crypro_balance, fiat_balance = 0, 0
    trading_result = {}

    with open(data_file_name, "r") as log_file:
        operations_logs = json.load(log_file)

    for day in operations_logs:

        if day.get("bought"):
            crypro_balance += Decimal(day["bought"])
            fiat_balance -= (
                Decimal(day["bought"]) * Decimal(day["matecoin_price"])
            )

        if day.get("sold"):
            crypro_balance -= Decimal(day["sold"])
            fiat_balance += (
                Decimal(day["sold"]) * Decimal(day["matecoin_price"])
            )

            trading_result.update(
                {
                    "earned_money": str(fiat_balance),
                    "matecoin_account": str(crypro_balance)
                }
            )

        with open("profit.json", "w") as result_json_file:
            json.dump(trading_result, result_json_file, indent=2)
