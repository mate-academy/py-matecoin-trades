import json
from decimal import Decimal


def calculating_earned_money_and_matecoin_account(trades: list) -> dict:
    sold_total = Decimal("0")
    bought_total = Decimal("0")
    stock = Decimal("0")
    for trade in trades:

        if trade["sold"] is not None:
            stock -= Decimal(trade["sold"])
            sold_total += (Decimal(trade["sold"])
                           * Decimal(trade["matecoin_price"]))
        if trade["bought"] is not None:
            stock += Decimal(trade["bought"])
            bought_total += (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
    return {
        "earned_money": str(Decimal(sold_total) - Decimal(bought_total)),
        "matecoin_account": str(stock)}


def calculate_profit(trades_filename: str) -> None:
    with open(trades_filename, "r") as trades_json:
        trades = json.load(trades_json)
        for_test = Decimal("0")
        print(for_test)
        profit = calculating_earned_money_and_matecoin_account(trades)
        with open("profit.json", "w") as profit_json:
            json.dump(profit, profit_json, indent=2)
