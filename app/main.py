import json
from decimal import Decimal, ROUND_DOWN


def calculate_profit(trades_file: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(trades_file, "r") as file:
        trades = json.load(file)

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade.get("matecoin_price", "0"))

        if bought:
            bought_volume = Decimal(bought)
            cost = (bought_volume * matecoin_price).quantize(
                Decimal("0.00000001"), rounding=ROUND_DOWN
            )
            earned_money -= cost
            matecoin_account += bought_volume
        if sold:
            sold_volume = Decimal(sold)
            revenue = (sold_volume * matecoin_price).quantize(
                Decimal("0.00000001"), rounding=ROUND_DOWN
            )
            earned_money += revenue
            matecoin_account -= sold_volume

    profit_data = {
        "earned_money": str(
            earned_money.quantize(
                Decimal("0.00000001"), rounding=ROUND_DOWN
            ).normalize()
        ),
        "matecoin_account": str(
            matecoin_account.quantize(
                Decimal("0.00001"), rounding=ROUND_DOWN
            ).normalize()
        ),
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
