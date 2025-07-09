import json
import decimal
from pathlib import Path


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        json_data = json.load(f)

    bought_profit = decimal.Decimal("0")
    sold_profit = decimal.Decimal("0")
    bought = decimal.Decimal("0")
    sold = decimal.Decimal("0")

    for operations in json_data:
        if operations["bought"] is not None:
            bought_profit += (decimal.Decimal(operations["bought"])
                              * decimal.Decimal(operations["matecoin_price"]))
            bought += decimal.Decimal(operations["bought"])
        if operations["sold"] is not None:
            sold_profit += (decimal.Decimal(operations["sold"])
                            * decimal.Decimal(operations["matecoin_price"]))
            sold += decimal.Decimal(operations["sold"])

    profit = sold_profit - bought_profit
    matecoin = bought - sold

    profit_data = {"earned_money": str(profit),
                   "matecoin_account": str(matecoin)}
    output_path = Path(__file__).resolve().parent.parent / "profit.json"

    with open(output_path, "w") as f:
        json.dump(profit_data, f, indent=2)
