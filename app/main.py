import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f_trades:
        matecoins_bought = Decimal("0")
        matecoins_sold = Decimal("0")
        total_bought = Decimal("0")
        total_sold = Decimal("0")

        for info in json.load(f_trades):
            if info.get("bought") is not None:
                matecoins_bought += (
                    Decimal(info["bought"]) * Decimal(info["matecoin_price"])
                )
            if info.get("sold") is not None:
                matecoins_sold += (
                    Decimal(info["sold"]) * Decimal(info["matecoin_price"])
                )
            total_bought += Decimal(info.get("bought") or 0)
            total_sold += Decimal(info.get("sold") or 0)

    with open("profit.json", "w") as f_profit:
        operation = {
            "earned_money": str(matecoins_sold - matecoins_bought),
            "matecoin_account": str(total_bought - total_sold)
        }
        json.dump(operation, f_profit, indent=2)
