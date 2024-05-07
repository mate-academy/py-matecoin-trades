import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades_data = json.load(f)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trades in trades_data:
        if trades["bought"] is not None:
            bought = Decimal(trades["bought"])
            matecoin_price = Decimal(trades["matecoin_price"])
            earned_money -= bought * matecoin_price
            matecoin_account += bought
        if trades["sold"] is not None:
            sold = Decimal(trades["sold"])
            matecoin_price = Decimal(trades["matecoin_price"])
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit_data, f, indent=2)
