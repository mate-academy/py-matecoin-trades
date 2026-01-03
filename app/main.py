import json
from decimal import Decimal


def calculate_profit(trades_file_path):
    with open(trades_file_path, "r") as file:
        trades_data = json.load(file)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        if trade.get("bought") is not None:
            volume = Decimal(trade["bought"])
            preco = Decimal(trade["matecoin_price"])
            earned_money -= volume * preco
            matecoin_account += volume
        if trade.get("sold") is not None:
            volume = Decimal(trade["sold"])
            preco = Decimal(trade["matecoin_price"])
            earned_money += volume * preco
            matecoin_account -= volume

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)

    return None
