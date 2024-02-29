import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        trades_data = json.load(file)

    trade_result = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    for trade in trades_data:
        trade_bought = (
            Decimal(trade.get("bought"))
            if trade.get("bought") else Decimal("0")
        )
        trade_sold = (
            Decimal(trade.get("sold"))
            if trade.get("sold") else Decimal("0")
        )
        trade_matecoin_price = Decimal(trade.get("matecoin_price"))

        earned_money = (trade_sold - trade_bought) * trade_matecoin_price
        matecoin_account = trade_bought - trade_sold

        trade_result["earned_money"] += earned_money
        trade_result["matecoin_account"] += matecoin_account

    trade_result = {
        "earned_money": str(trade_result["earned_money"]),
        "matecoin_account": str(trade_result["matecoin_account"])
    }

    with open("profit.json", "w") as file:
        json.dump(trade_result, file, indent=2)
