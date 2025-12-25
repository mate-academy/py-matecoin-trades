import json
from decimal import Decimal


def calculate_profit(file_path: json) -> None:
    with open(file_path, "r") as file:
        trades = json.load(file)

    result = {}
    earned_money = Decimal("0")
    current_coins_amount = Decimal("0")

    for trade in trades:
        coins_bought = Decimal(trade.get("bought")) \
            if trade.get("bought") is not None else Decimal(0)
        coins_sold = Decimal(trade.get("sold")) \
            if trade.get("sold") is not None else Decimal(0)
        price = Decimal(trade.get("matecoin_price"))

        earned_money += (coins_sold - coins_bought) * price
        current_coins_amount += coins_bought - coins_sold

        result["earned_money"] = str(earned_money)
        result["matecoin_account"] = str(current_coins_amount)

    with open("profit.json", "w") as final:
        json.dump(result, final, indent=2)
