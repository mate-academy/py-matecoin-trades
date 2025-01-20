import json
import decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as file_json:
        trades = json.load(file_json)

        coins = decimal.Decimal(0.0)
        earned = decimal.Decimal(0.0)

        for trade in trades:
            if trade["bought"] is not None:
                earned -= decimal.Decimal(trade["bought"]) \
                    * decimal.Decimal(trade["matecoin_price"])
                coins += decimal.Decimal(trade["bought"])
            if trade["sold"] is not None:
                earned += decimal.Decimal(trade["sold"]) \
                    * decimal.Decimal(trade["matecoin_price"])
                coins -= decimal.Decimal(trade["sold"])

    with open("profit.json", "w") as profit_json:
        json.dump({"earned_money": str(earned),
                   "matecoin_account": str(coins)}, profit_json, indent=2)
