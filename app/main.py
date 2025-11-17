import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    matecoin_account, earned_money = 0, 0
    with open(filename, "r") as f:
        trades = f.read()
    trades = json.loads(trades)
    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = Decimal(trade["bought"]) if trade["bought"] else 0
        sold = Decimal(trade["sold"]) if trade["sold"] else 0
        matecoin_account += bought
        matecoin_account -= sold
        earned_money += price * bought - price * sold
    with open("profit.json", "w") as f:
        f.write(
            json.dumps(
                {
                    "earned_money": f"{earned_money}",
                    "matecoin_account": f"{matecoin_account}",
                }
            )
        )
