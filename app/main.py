import json
from decimal import Decimal
import os


def calculate_profit(file_name: str) -> dict:
    with open(file_name, "r") as file:
        trades_data = json.load(file)

    profit = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        bought = Decimal(trade.get("bought", "0") or "0")
        sold = Decimal(trade.get("sold", "0") or "0")
        matecoin_price = Decimal(trade.get("matecoin_price", "0") or "0")

        if bought > 0:
            cost = bought * matecoin_price
            matecoin_account += bought
            profit -= cost
        if sold > 0:
            revenue = sold * matecoin_price
            matecoin_account -= sold
            profit += revenue

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)


print("Current Working Directory:", os.getcwd())
