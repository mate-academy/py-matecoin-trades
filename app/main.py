import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as source_file:
        profit_dict = dict()
        trades_list = json.load(source_file)

        for trade in trades_list:

            earned_money_result = Decimal(
                profit_dict.get("earned_money", "0")
            )

            matecoin_account_result = Decimal(
                profit_dict.get("matecoin_account", "0")
            )
            if trade["sold"] is not None:
                matecoin_account_result -= Decimal(trade["sold"])
                earned_money_result += (
                + Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
                )

                profit_dict.update(
                    {
                        "earned_money": str(earned_money_result),
                        "matecoin_account": str(matecoin_account_result)
                    }
                )

            if trade["bought"] is not None:
                matecoin_account_result += Decimal(trade["bought"])
                earned_money_result += (
                - Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
                )
                profit_dict.update(
                    {
                        "earned_money": str(earned_money_result),
                        "matecoin_account": str(matecoin_account_result)
                    }
                )

    with open("profit.json", "w") as write_file:
        json.dump(profit_dict, write_file, indent=2)
