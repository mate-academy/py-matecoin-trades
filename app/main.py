from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(file_name) as f:
        coin_data = json.load(f)
        for operation in coin_data:
            buy = operation["bought"]
            sell = operation["sold"]
            price = operation["matecoin_price"]
            if buy:
                matecoin_account += Decimal(buy)
                earned_money -= Decimal(buy) * Decimal(price)
            if sell:
                matecoin_account -= Decimal(sell)
                earned_money += Decimal(sell) * Decimal(price)
    with open("profit.json", "w") as f:
        json.dump({"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}, f, indent=2)
