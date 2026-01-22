from decimal import Decimal
import json


def calculate_profit(trades_file_name: str) -> None:
    with open(trades_file_name, "r") as trades_open:
        trade_sessions = json.load(trades_open)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trade_sessions:
        if trade.get("bought") is not None:
            earned_money -= (Decimal(trade.get("bought"))
                             * Decimal(trade.get("matecoin_price")))
            matecoin_account += Decimal(trade.get("bought"))

        if trade.get("sold") is not None:
            earned_money += (Decimal(trade.get("sold"))
                             * Decimal(trade.get("matecoin_price")))
            matecoin_account -= Decimal(trade.get("sold"))

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
