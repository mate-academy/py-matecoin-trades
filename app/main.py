import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    with open(file_name) as trades_file:
        operations = json.load(trades_file)

    for trade in operations:
        if "bought" in trade and trade["bought"]:
            earned_money -= (Decimal(str(trade["bought"]))
                             * Decimal(str(trade["matecoin_price"])))
            matecoin_account += Decimal(str(trade["bought"]))
        if "sold" in trade and trade["sold"]:
            earned_money -= (Decimal(str(trade["sold"]))
                             * Decimal(str(trade["matecoin_price"])))
            matecoin_account += Decimal(str(trade["sold"]))

    profit_dict = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as profit_file:
        json.dump(profit_dict, profit_file, indent=2)
