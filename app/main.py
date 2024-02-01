import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as f:
        trades = json.load(f)

    total_profit = Decimal(0)
    current_coins = Decimal(0)

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        bought_volume = (Decimal(trade.get("bought")) if
                         trade.get("bought") is not None else 0)
        sold_volume = (Decimal(trade.get("sold")) if
                       trade.get("sold") is not None else 0)

        current_coins += bought_volume - sold_volume
        total_profit += (sold_volume * matecoin_price
                         - bought_volume * matecoin_price)

    profit_data = {
        "earned_money": str(total_profit),
        "matecoin_account": str(current_coins)
    }

    with open("profit.json", "w") as profit:
        json.dump(profit_data, profit, indent=2)
