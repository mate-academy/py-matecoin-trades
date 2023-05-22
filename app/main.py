from json import load, dump
from decimal import Decimal


def calculate_profit(url: str) -> None:
    with open(url, "r") as f:
        trade_data = load(f)

    profit = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    for transaction in trade_data:
        current_price = Decimal(transaction["matecoin_price"])
        current_trade = Decimal(
            transaction["bought"] or ("-" + transaction["sold"])
        )

        profit["matecoin_account"] += current_trade
        profit["earned_money"] -= current_trade * current_price

    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])
    with open("profit.json", "w") as f:
        dump(profit, f, indent=2)
