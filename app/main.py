import json
from decimal import Decimal


def calculate_profit(name_of_the_file: str) -> None:
    with open(name_of_the_file, "r") as trades_file:
        trades_data = json.load(trades_file)

    earned_money, matecoin_account = 0, 0

    for operation in trades_data:
        if operation["bought"] is not None:
            earned_money -= (
                Decimal(operation["bought"])
                * Decimal(operation["matecoin_price"])
            )
            matecoin_account += Decimal(operation["bought"])
        if operation["sold"] is not None:
            earned_money += (
                Decimal(operation["sold"])
                * Decimal(operation["matecoin_price"])
            )
            matecoin_account -= Decimal(operation["sold"])

    result_trades = {
        "earned_money": f"{earned_money}",
        "matecoin_account": f"{matecoin_account}"
    }

    with open("profit.json", "w") as trades_to_write:
        json.dump(result_trades, trades_to_write, indent=2)
