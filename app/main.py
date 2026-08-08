import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    if file_path is None or not isinstance(file_path, str):
        return

    with open(file_path, "r") as json_trades:
        trades = json.load(json_trades)

    matecoin_account = Decimal("0.0")
    earned_money = Decimal("0.0")

    for trade in trades:
        if (trade["bought"] is not None
                and isinstance(trade["bought"], str)):

            matecoin_account += Decimal(trade["bought"])
            cost = (Decimal(trade["bought"])
                    * Decimal(trade["matecoin_price"]))
            earned_money -= cost

        if (trade["sold"] is not None
                and isinstance(trade["sold"], str)):

            matecoin_account -= Decimal(trade["sold"])
            revenue = (Decimal(trade["sold"])
                       * Decimal(trade["matecoin_price"]))
            earned_money += revenue

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file, indent=2)
