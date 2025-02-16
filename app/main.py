import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)
        profit = {"earned_money": 0, "matecoin_account": 0}

    for trade in trades:
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            profit["matecoin_account"] += bought
            profit["earned_money"] -= bought * Decimal(trade["matecoin_price"]
        if trade["sold']:
            sold = Decimal(trade["sold"])
            profit["earned_money"] -= sold
            profit["earned_money"] += sold * Decimal(trade["matecoin_price"]
            
    result = {
        "earned_money": str(profit["earned_money"]),
        "matecoin_account": str(profit["matecoin_account"])
    }
    
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
