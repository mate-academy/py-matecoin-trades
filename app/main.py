import decimal
import json


def calculate_profit(name_of_the_file: str) -> None:
    with open(name_of_the_file, "r") as file:
        trades_info = json.load(file)

    profit = 0
    coins_on_account = 0

    for trade in trades_info:
        if trade.get("bought"):
            profit -= (
                decimal.Decimal(trade.get("bought"))
                * decimal.Decimal(trade.get("matecoin_price"))
            )
            coins_on_account += decimal.Decimal(trade.get("bought"))

        if trade.get("sold"):
            profit += (
                decimal.Decimal(trade.get("sold"))
                * decimal.Decimal(trade.get("matecoin_price"))
            )
            coins_on_account -= decimal.Decimal(trade.get("sold"))

    result_of_trades = {
        "earned_money": str(profit),
        "matecoin_account": str(coins_on_account)
    }
    with open("profit.json", "w") as file:
        json.dump(result_of_trades, file, indent=2)
