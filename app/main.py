import json
from decimal import Decimal


def calculate_profit(trades_file: json) -> None:
    with open(trades_file, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for deal in trades:
        if deal["bought"]:
            matecoin_account += Decimal(deal["bought"])
            earned_money -= (Decimal(deal["bought"])
                             * Decimal(deal["matecoin_price"]))
        if deal["sold"]:
            matecoin_account -= Decimal(deal["sold"])
            earned_money += (Decimal(deal["sold"])
                             * Decimal(deal["matecoin_price"]))

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
