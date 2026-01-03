import json

from decimal import Decimal
from pathlib import Path


def calculate_profit(
        file_name: str,
        output_file: str = "profit.json"
) -> None:
    total_bought = Decimal("0.0")
    total_spent = Decimal("0.0")
    total_sold = Decimal("0.0")
    total_earned = Decimal("0.0")

    res_dict = {}

    with open(file_name, "r") as file:
        deserial_data = json.load(file)

    for trade_operation in deserial_data:

        bought = trade_operation.get("bought")
        sold = trade_operation.get("sold")
        price = trade_operation.get("matecoin_price")

        if bought:
            total_bought += Decimal(bought)
            total_spent += (Decimal(bought) * Decimal(price))

        if sold:
            total_sold += Decimal(sold)
            total_earned += (Decimal(sold) * Decimal(price))

    res_dict["earned_money"] = str(total_earned - total_spent)
    res_dict["matecoin_account"] = str(total_bought - total_sold)

    output_path = Path(file_name).resolve().parent.parent / output_file
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as file_output:
        json.dump(res_dict, file_output, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
