import json
from decimal import Decimal


def calculate_profit(trades_path: str) -> None:
    if trades_path is None or not isinstance(trades_path, str):
        return

    with open(trades_path, "r") as json_trades:
        trades = json.load(json_trades)

    matecoin_account = Decimal("0.0")
    earned_money = Decimal("0.0")

    for trade in trades:
        if (
                trade.get("bought") is not None
                and isinstance(trade.get("bought"), str)
        ):
            matecoin_account += Decimal(trade.get("bought"))
            cost = (
                Decimal(trade.get("bought"))
                * Decimal(trade.get("matecoin_price"))
            )
            earned_money -= cost
        if (
            trade.get("sold") is not None
            and isinstance(trade.get("sold"), str)
        ):
            matecoin_account -= Decimal(trade.get("sold"))
            revenue = (
                Decimal(trade.get("sold"))
                * Decimal(trade.get("matecoin_price"))
            )
            earned_money += revenue

    final_result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as profit_file:
        json.dump(final_result, profit_file, indent=2)


calculate_profit(trades_path="app/trades.json")
