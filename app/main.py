import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as f:
        fail_trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for i in fail_trades:
        bought_coin = Decimal(i.get("bought") or 0)
        sold_coin = Decimal(i.get("sold") or 0)
        matecoin_price = Decimal(i.get("matecoin_price") or 0)

        if bought_coin > 0:
            earned_money -= bought_coin * matecoin_price
            matecoin_account += bought_coin

        if sold_coin > 0:
            earned_money += sold_coin * matecoin_price
            matecoin_account -= sold_coin

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as output_file:
            json.dump(result, output_file, indent=2)
