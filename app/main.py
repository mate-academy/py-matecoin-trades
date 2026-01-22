import json
from decimal import Decimal
import os


def calculate_profit(file_name: str) -> None:
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, file_name)

    if not os.path.exists(file_path):
        print(f"Error: The file '{file_name}' does not exist.")
        return

    with open(file_path, "r") as f:
        trades = json.load(f)

    total_bought = Decimal(0)
    total_sold = Decimal(0)

    for trade in trades:
        if trade["bought"] is not None:
            total_bought += (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
        if trade["sold"] is not None:
            total_sold += (Decimal(trade["sold"])
                           * Decimal(trade["matecoin_price"]))

    earned_money = total_sold - total_bought
    matecoin_account = sum(Decimal(trade["bought"] or 0)
                           - Decimal(trade["sold"] or 0) for trade in trades)

    profit_info = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    project_dir = os.path.dirname(os.path.dirname(current_dir))
    profit_file_path = os.path.join(project_dir, "profit.json")

    with open(profit_file_path, "w", encoding="utf-8") as f:
        json.dump(profit_info, f, indent=4)


calculate_profit("trades.json")
