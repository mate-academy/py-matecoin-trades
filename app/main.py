import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as f:
        trades = json.load(f)

    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade.get("matecoin_price"))

        print(f"Trade: {trade}")

        if bought:
            bought_amount = Decimal(bought)
            matecoin_account += bought_amount
            earned_money -= bought_amount * matecoin_price
            print(
                f"Bought: {bought_amount}, "
                f"matecoin_account: {matecoin_account}, "
                f"earned_money: {earned_money}"
            )
        if sold:
            sold_amount = Decimal(sold)
            matecoin_account -= sold_amount
            earned_money += sold_amount * matecoin_price
            print(
                f"Sold: {sold_amount}, "
                f"matecoin_account: {matecoin_account}, "
                f"earned_money: {earned_money}"
            )

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit_data, f, indent=2)
