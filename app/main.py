import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades_list = json.load(file)
    bought = Decimal("0.0")
    sold = Decimal("0.0")
    profit = Decimal("0.0")
    expenses = Decimal("0.0")
    for el in trades_list:
        if el.get("bought") is not None:
            bought += Decimal(el.get("bought"))
            expenses += (Decimal(el.get("bought"))
                         * Decimal(el.get("matecoin_price")))
        if el.get("sold") is not None:
            sold += Decimal(el.get("sold"))
            profit += (Decimal(el.get("sold"))
                       * Decimal(el.get("matecoin_price")))

    earned_money = profit - expenses
    matecoin_account = Decimal(bought - sold)

    profit_file = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as file_to_write:
        json.dump(profit_file, file_to_write, indent=2)
