from decimal import Decimal
import json


def calculate_profit(trade_info_file_name: str) -> None:
    with open(trade_info_file_name) as json_file:
        data = json.load(json_file)
        print(data)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in data:
        price = Decimal(str(trade["matecoin_price"]))
        if trade.get("bought") is not None:
            qty = Decimal(str(trade["bought"]))
            earned_money -= price * qty
            matecoin_account += qty
        if trade.get("sold") is not None:
            qty = Decimal(str(trade["sold"]))
            earned_money += price * qty
            matecoin_account -= qty

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as json_file:
        json.dump(result, json_file, indent=2)
