import json
from decimal import Decimal


def calculate_profit(trades_file_name: str) -> None:
    with open(trades_file_name) as trade_file:
        trades = json.load(trade_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(str(trade.get("matecoin_price", 0)))

        bought = trade.get("bought")
        if bought is not None:
            amount = Decimal(str(bought))
            earned_money -= amount * price
            matecoin_account += amount

        sold = trade.get("sold")
        if sold is not None:
            amount = Decimal(str(sold))
            earned_money += amount * price
            matecoin_account -= amount

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
