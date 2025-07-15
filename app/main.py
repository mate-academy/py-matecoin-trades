import json
from decimal import Decimal as D


def calculate_profit(filename: str) -> None:
    purchase, sale, coin_count = D("0"), D("0"), D("0")

    with open(filename, "r") as json_trades:
        trades = json.load(json_trades)

        for trade in trades:
            if trade.get("bought") is not None:
                purchase += D(trade["bought"]) * D(trade["matecoin_price"])
                coin_count += D(trade["bought"])
            if trade.get("sold") is not None:
                sale += D(trade["sold"]) * D(trade["matecoin_price"])
                coin_count -= D(trade["sold"])

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
