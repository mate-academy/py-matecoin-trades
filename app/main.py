from decimal import Decimal
import json
import os
from pathlib import Path


def calculate_profit(file_name: str) -> None:
    bought, sold, matecoin_price = "bought", "sold", "matecoin_price"

    with open(file_name) as j_data:
        data = json.load(j_data)

    account = Decimal("0.0")
    profit = Decimal("0.0")
    for transaction in data:
        course = Decimal(transaction[matecoin_price])
        if transaction[bought]:
            buy_count = Decimal(transaction[bought]) * course
            account += Decimal(transaction[bought])
            profit -= buy_count

        if transaction[sold]:
            sold_count = Decimal(transaction[sold])
            account -= sold_count
            profit += sold_count * course

    output = {
        "earned_money": str(profit),
        "matecoin_account": str(account)
    }

    base_dir = Path(__file__).resolve().parent.parent
    profit_path = os.path.join(base_dir, "profit.json")

    with open(profit_path, "w") as j_file:
        json.dump(output, j_file, indent=2)


if __name__ == '__main__':
    calculate_profit("trades.json")
