import json
import os
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    result_bought = Decimal("0")
    result_sold = Decimal("0")
    total_bought = Decimal("0")
    total_sold = Decimal("0")
    with open(file_name, "r") as file_out:
        python_file = json.load(file_out)
        for dicts in python_file:
            if dicts["bought"] is not None:
                result_bought += Decimal(dicts["bought"])
                total_bought += Decimal(dicts["bought"]) * \
                    Decimal(dicts["matecoin_price"])
            if dicts["sold"] is not None:
                result_sold += Decimal(dicts["sold"])
                total_sold += Decimal(dicts["sold"]) * \
                    Decimal(dicts["matecoin_price"])
            end_result = {"earned_money": str(total_sold - total_bought),
                          "matecoin_account": str(result_bought - result_sold)}
            os.makedirs("app/profit.json", exist_ok=True)
            with open("profit.json", "w") as file_in:
                json.dump(end_result,
                          file_in,
                          ensure_ascii=False,
                          default=str,
                          indent=2)
