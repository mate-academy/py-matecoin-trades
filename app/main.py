import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as f:
        trades_data = json.load(f)

    all_bought = Decimal("0.0")
    all_sold = Decimal("0.0")
    profit = Decimal("0.0")
    for i in range(len(trades_data)):
        if trades_data[i]["bought"] is not None:
            bought_today = Decimal(trades_data[i]["bought"])
        else:
            bought_today = Decimal("0.0")
        if trades_data[i]["sold"] is not None:
            sold_today = Decimal(trades_data[i]["sold"])
        else:
            sold_today = Decimal("0.0")
        profit += ((sold_today - bought_today)
                   * Decimal(trades_data[i]["matecoin_price"]))
        all_bought += bought_today
        all_sold += sold_today

    profit_data = {
        "earned_money" : str(profit),
        "matecoin_account" : str(all_bought - all_sold)
    }

    with open("profit.json" , "w") as f:
        json.dump(profit_data, f, indent=2)
