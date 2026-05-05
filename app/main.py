from decimal import Decimal
import json


def calculate_profit(
        trade_file: str,
        profit_file: str | None = None
) -> None:
    with open(trade_file, "r") as read_file:
        trade_data = json.load(read_file)
    profit = Decimal("0")
    matecoins = Decimal("0")
    for trade in trade_data:
        price = Decimal(trade["matecoin_price"])
        if trade["sold"] is not None:
            coins = Decimal(trade["sold"])
            matecoins -= coins
            profit += coins * price
        if trade["bought"] is not None:
            coins = Decimal(trade["bought"])
            matecoins += coins
            profit -= coins * price
    write_data = {"earned_money": str(profit),
                  "matecoin_account": str(matecoins)}
    profit_file = profit_file or "profit.json"
    with open(profit_file, "w") as write_file:
        json.dump(write_data, write_file, indent=2)
