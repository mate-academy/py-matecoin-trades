import json
from decimal import Decimal


def calculate_profit(trades_info_data: str) -> None:
    with open(trades_info_data) as file:
        trades_data = json.load(file)
    earned_money = 0
    matecoin_account = 0
    for el in trades_data:
        bought = el["bought"]
        sold = el["sold"]
        matecoin_price = el["matecoin_price"]
        if bought:
            matecoin_account += Decimal(bought)
            earned_money -= Decimal(bought) * Decimal(matecoin_price)
        if sold:
            matecoin_account -= Decimal(sold)
            earned_money += Decimal(sold) * Decimal(matecoin_price)
    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
