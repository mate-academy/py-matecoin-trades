import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades_info = json.load(file)

    profit = 0
    coin = 0

    for trade in trades_info:
        if trade.get("bought"):
            profit -= (
                decimal.Decimal(trade.get("bought"))
                * decimal.Decimal(trade.get("matecoin_price"))
            )
            coin += decimal.Decimal(trade.get("bought"))

        if trade.get("sold"):
            profit += (
                decimal.Decimal(trade.get("sold"))
                * decimal.Decimal(trade.get("matecoin_price"))
            )
            coin -= decimal.Decimal(trade.get("sold"))

            resut = {
                "earned_money": str(profit),
                "matecoin_account": str(coin)
            }

            with open("profit.json", "w") as file:
                json.dump(resut, file, indent=2)
