import json
import decimal


def calculate_profit(name: str) -> None:
    with (open(name, "r") as f, open("profit.json", "w") as profit_file):
        trades = json.load(f)
        coin = 0
        bought_money = 0
        sold_money = 0
        for trade in trades:
            if trade["bought"] is not None:
                bought_money += (decimal.Decimal(trade["bought"])
                                 * decimal.Decimal(trade["matecoin_price"]))
                coin += decimal.Decimal(trade["bought"])
            if trade["sold"] is not None:
                sold_money += (decimal.Decimal(trade["sold"])
                               * decimal.Decimal(trade["matecoin_price"]))
                coin -= decimal.Decimal(trade["sold"])

        earned_money = (decimal.Decimal(sold_money)
                        - decimal.Decimal(bought_money))

        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(coin)
            },
            profit_file,
            indent=3
        )
