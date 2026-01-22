import json
from decimal import Decimal


def calculate_profit(input_file: str,
                     output_file: str = "profit.json") -> None:
    with open(input_file, "r") as f:
        trades = json.load(f)

    earning = 0
    coin_account = 0

    for trade in trades:
        trade = {key: Decimal(value) if value is not None else Decimal(0)
                 for key, value in trade.items()}

        earning -= trade["bought"] * trade["matecoin_price"]
        earning += trade["sold"] * trade["matecoin_price"]

        coin_account += trade["bought"]
        coin_account -= trade["sold"]

    wallet = {"earned_money": str(earning),
              "matecoin_account": str(coin_account)}

    with open(output_file, "w") as f:
        json.dump(wallet, f, indent=2)
