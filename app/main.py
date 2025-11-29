import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    try:
        with open(file_name, "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []
    profit = {"earned_money": Decimal("0"), "matecoin_account": Decimal("0")}
    for trade in data:
        bought = (Decimal(trade.get("bought"))
                  if trade.get("bought") is not None else None)
        sold = (Decimal(trade.get("sold"))
                if trade.get("sold") is not None else None)
        matecoin_price = Decimal(trade.get("matecoin_price", "0"))
        if bought is not None:
            profit["earned_money"] -= bought * matecoin_price
            profit["matecoin_account"] += bought
        if sold is not None:
            profit["earned_money"] += sold * matecoin_price
            profit["matecoin_account"] -= sold
    profit_str = {key: str(value) for key, value in profit.items()}
    with open("profit.json", "w") as json_file:
        json.dump(profit_str, json_file, indent=2)
