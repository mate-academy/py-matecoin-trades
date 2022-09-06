import json
from decimal import Decimal


def calculate_profit(name_json):
    with open(name_json) as f:
        trades = json.load(f)
    earning = 0
    coin_account = 0
    for trade in trades:

        trade = {key: value if value is not None else "0"
                 for key, value in trade.items()}

        earning -= Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
        earning += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])

        coin_account += Decimal(trade["bought"])
        coin_account -= Decimal(trade["sold"])

    wallet = {"earned_money": str(earning),
              "matecoin_account": str(coin_account)}
    with open("profit.json", "w") as f:
        json.dump(wallet, f, indent=2)
