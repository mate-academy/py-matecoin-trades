import json
from decimal import Decimal
from typing import List, Dict


def calculate_profit(file_name: str) -> None:
    try:
        with open(file_name, "r") as file:
            trades: List[Dict[str, str]] = json.load(file)

        earned_money = Decimal("0.0")
        matecoin_account = Decimal("0.0")

        for trade in trades:
            if trade["bought"] is not None:
                matecoin_account += Decimal(trade["bought"])
                earned_money -= Decimal(
                    trade["bought"]) * Decimal(trade["matecoin_price"]
                                               )
            if trade["sold"] is not None:
                matecoin_account -= Decimal(trade["sold"])
                earned_money += Decimal(
                    trade["sold"]) * Decimal(trade["matecoin_price"]
                                             )

        profit_data = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }

        with open("profit.json", "w") as output_file:
            json.dump(profit_data, output_file, indent=2)

    except Exception as e:
        print(f"Error occurred: {e}")
        return None
