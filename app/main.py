import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    networth = Decimal("0")
    coin_amount = Decimal("0")

    for trade in trades:
        bought = Decimal(trade.get("bought") or "0")
        sold = Decimal(trade.get("sold") or "0")
        price = Decimal(trade.get("matecoin_price") or "0")

        # handle both independently
        if bought:
            networth -= bought * price
            coin_amount += bought

        if sold:
            networth += sold * price
            coin_amount -= sold

    result_dict = {
        "earned_money": str(networth),
        "matecoin_account": str(coin_amount)
    }

    with open("profit.json", "w") as file:
        json.dump(result_dict, file, indent=2)
