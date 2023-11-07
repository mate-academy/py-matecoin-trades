import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        content = json.load(file)

    bought = Decimal(0)
    sold = Decimal(0)
    mate_bought = Decimal(0)
    mate_sold = Decimal(0)

    for trade in content:
        if trade.get("bought") is None:
            trade["bought"] = 0
        elif trade.get("sold") is None:
            trade["sold"] = 0

        start_bought = Decimal(trade.get("bought"))
        start_sold = Decimal(trade.get("sold"))
        mate_price = Decimal(trade.get("matecoin_price"))

        bought += start_bought
        sold += start_sold

        mate_bought += start_bought * mate_price
        mate_sold += start_sold * mate_price

    profit = {
        "earned_money": f"{mate_sold - mate_bought}",
        "matecoin_account": f"{bought - sold}"
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
