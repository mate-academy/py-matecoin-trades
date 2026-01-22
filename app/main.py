from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file_in:
        trades = json.load(file_in)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade.get("bought") is not None:
            bought = Decimal(trade.get("bought"))
            matecoin_price = Decimal(trade.get("matecoin_price"))
            matecoin_account += bought
            earned_money -= bought * matecoin_price
        if trade.get("sold") is not None:
            sold = Decimal(trade.get("sold"))
            matecoin_price = Decimal(trade.get("matecoin_price"))
            matecoin_account -= sold
            earned_money += sold * matecoin_price

    json_profit = {}
    json_profit["earned_money"] = str(earned_money)
    json_profit["matecoin_account"] = str(matecoin_account)

    with open("profit.json", "w") as file_out:
        json.dump(json_profit, file_out, indent=2)
