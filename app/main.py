import json
from decimal import Decimal


def calculate_profit(file_name: str) -> dict:
    with open(file_name) as f:
        trades = json.load(f)

    wallet = {"earned_money": Decimal("0"), "matecoin_account": Decimal("0")}

    for trade in trades:
        if trade["bought"] is None and trade["sold"] is not None:
            wallet["earned_money"] += Decimal(trade["sold"]) * Decimal(
                trade["matecoin_price"]
            )
            wallet["matecoin_account"] -= Decimal(trade["sold"])
        elif trade["sold"] is None and trade["bought"] is not None:
            wallet["earned_money"] -= Decimal(trade["bought"]) * Decimal(
                trade["matecoin_price"]
            )
            wallet["matecoin_account"] += Decimal(trade["bought"])
        else:
            wallet["earned_money"] += Decimal(trade["sold"]) * Decimal(
                trade["matecoin_price"]
            )
            wallet["matecoin_account"] -= Decimal(trade["sold"])
            wallet["earned_money"] -= Decimal(trade["bought"]) * Decimal(
                trade["matecoin_price"]
            )
            wallet["matecoin_account"] += Decimal(trade["bought"])

    print(wallet)

    with open("profit.json", "w") as profit_file:
        json.dump(
            {key: str(value) for key, value in wallet.items()},
            profit_file,
            indent=2,
        )
