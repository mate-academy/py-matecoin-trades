import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    purchase, sale, coin_count = (
        Decimal("0"),
        Decimal("0"),
        Decimal("0")
    )

    with open(filename, "r") as json_trades:
        trades = json.load(json_trades)

        for trade in trades:
            price = Decimal(trade["matecoin_price"])

            if trade.get("bought") is not None:
                bought_amount = Decimal(trade["bought"])
                purchase += bought_amount * price
                coin_count += bought_amount
            if trade.get("sold") is not None:
                sold_amount = Decimal(trade["sold"])
                sale += sold_amount * price
                coin_count -= sold_amount

    with open("../profit.json", "w") as json_profit:
        profit = sale - purchase
        json_result = {
            "earned_money": str(profit),
            "matecoin_account": str(coin_count)
        }
        json.dump(json_result, json_profit, indent=2)
