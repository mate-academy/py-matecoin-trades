import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file) as source_file:
        data_trades = json.load(source_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in data_trades:
        bought = (
            Decimal(trade["bought"])
            if trade["bought"] is not None else Decimal("0")
        )
        sold = (
            Decimal(trade["sold"])
            if trade["sold"] is not None else Decimal("0")
        )
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought > 0:
            earned_money -= bought * matecoin_price
            matecoin_account += bought
        if sold > 0:
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as json_file:
        json.dump(profit_data, json_file, indent=4)


calculate_profit("trades.json")
