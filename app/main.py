from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    with open(filename) as file_in:
        trades_history = json.load(file_in)

    plbalance = 0
    mate_coins_wallet_balance = 0
    for trade in trades_history:
        if trade.get("sold"):
            mate_coins_wallet_balance -= Decimal(trade.get("sold"))
            plbalance += Decimal(trade.get("sold")) * Decimal(
                trade.get("matecoin_price")
            )
        if trade.get("bought"):
            mate_coins_wallet_balance += Decimal(trade.get("bought"))
            plbalance -= Decimal(trade.get("bought")) * Decimal(
                trade.get("matecoin_price")
            )

    data_dump = {
        "earned_money": str(plbalance),
        "matecoin_account": str(mate_coins_wallet_balance),
    }
    with open("profit.json", "w") as file_out:
        json.dump(data_dump, file_out, indent=2)
