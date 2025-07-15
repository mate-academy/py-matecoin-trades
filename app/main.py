import json
from decimal import Decimal as Dec


def calculate_profit(filename: str) -> None:
    purchase, sale, coin_count = Dec("0"), Dec("0"), Dec("0")

    with open(filename, "r") as json_trades:
        trades = json.load(json_trades)

        for trade in trades:
            if trade.get("bought") is not None:
                purchase += Dec(trade["bought"]) * Dec(trade["matecoin_price"])
                coin_count += Dec(trade["bought"])
            if trade.get("sold") is not None:
                sale += Dec(trade["sold"]) * Dec(trade["matecoin_price"])
                coin_count -= Dec(trade["sold"])

    with open("../profit.json", "w") as json_profit:
        profit = sale - purchase
        json.dump(
            {
                "earned_money": str(profit),
                "matecoin_account": str(coin_count)
            },
            json_profit,
            indent=2
        )
