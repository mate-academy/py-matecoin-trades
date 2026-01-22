import json
from decimal import Decimal


def calculate_profit(trades_f: list[object]) -> None:
    earned = 0
    matecoin_account = 0

    with open(trades_f, "r") as f:
        use_date = json.load(f)

    for trade in use_date:
        if trade["bought"]:
            earned -= (Decimal(trade["bought"])
                       * Decimal(trade["matecoin_price"]))
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"]:
            earned += (Decimal(trade["sold"])
                       * Decimal(trade["matecoin_price"]))
            matecoin_account -= Decimal(trade["sold"])

    result = {
        "earned_money": str(earned),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as new_f:
        json.dump(result, new_f, indent=2)
