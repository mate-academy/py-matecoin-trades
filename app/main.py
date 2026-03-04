import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)
    matecoin_account = Decimal(0)
    earned_money = Decimal(0)
    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = trade.get("matecoin_price")
        if bought:
            matecoin_account = matecoin_account + Decimal(bought)
            earned_money = earned_money - Decimal(bought) * Decimal(price)
        if sold:
            matecoin_account = matecoin_account - Decimal(sold)
            earned_money = earned_money + Decimal(sold) * Decimal(price)
    profit_string = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(profit_string, file, indent=2)
