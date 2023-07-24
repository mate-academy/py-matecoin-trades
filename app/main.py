from decimal import Decimal
import json
import os


def calculate_profit(name_trade_file: str) -> None:
    profit_result = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    with open(name_trade_file, "r") as file_trades_information:
        trades_information = json.load(file_trades_information)
        for trade in trades_information:
            bought = (
                Decimal(trade["bought"])
                if trade["bought"]
                else Decimal("0")
            )
            sold = (
                Decimal("-" + trade["sold"])
                if trade["sold"]
                else Decimal("0")
            )

            profit_result["earned_money"] += (
                (bought + sold) * Decimal(trade["matecoin_price"])
            )
            profit_result["matecoin_account"] += bought + sold

        profit_result["earned_money"] = (
            str(Decimal("-1") * profit_result["earned_money"])
        )
        profit_result["matecoin_account"] = (
            str(profit_result["matecoin_account"])
        )

    current_directory = os.getcwd()
    parent_directory = os.path.join(current_directory, "..")
    new_file_path = os.path.join(parent_directory, "profit.json")

    with open(
            new_file_path, "w"
    ) as file_profit:
        json.dump(profit_result, file_profit, indent=2)
