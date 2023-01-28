import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as file:
        info_trades = json.load(file)

    profit_trades = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    for one_trade in info_trades:
        if one_trade.get("bought") is not None:
            profit_trades["earned_money"] -= Decimal(one_trade["bought"]) \
                * Decimal(one_trade["matecoin_price"])
            profit_trades["matecoin_account"] += Decimal(one_trade["bought"])

        if one_trade.get("sold") is not None:
            profit_trades["earned_money"] += Decimal(one_trade["sold"]) \
                * Decimal(one_trade["matecoin_price"])
            profit_trades["matecoin_account"] -= Decimal(one_trade["sold"])

    profit_trades = {key: str(value) for key, value in profit_trades.items()}

    with open("profit.json", "w") as new_info_trades:
        json.dump(profit_trades, new_info_trades, indent=2)
