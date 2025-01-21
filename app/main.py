import json
import decimal


def calculate_profit(file_name: str) -> None:
    with (open(file_name) as file):
        trades = json.load(file)

        coins = decimal.Decimal(0.0)
        earn = decimal.Decimal(0.0)

        for trade in trades:
            if trade["bought"] is not None:
                earn -= decimal.Decimal(trade["bought"])\
                    * decimal.Decimal(trade["matecoin_price"])
                coins += decimal.Decimal(trade["bought"])
            if trade["sold"] is not None:
                earn += decimal.Decimal(trade["sold"])\
                    * decimal.Decimal(trade["matecoin_price"])
                coins -= decimal.Decimal(trade["sold"])

    with open("profit.json", "w") as profit_json:
        json.dump({"earned_money": str(earn),
                   "matecoin_account": str(coins)}, profit_json, indent=2)
