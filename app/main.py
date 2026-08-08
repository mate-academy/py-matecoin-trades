from decimal import Decimal

import json


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        trades_data = json.load(file)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")
    for transaction in trades_data:
        if transaction.get("bought") is not None:
            earned_money -= (Decimal(transaction.get("bought"))
                             * Decimal(transaction.get("matecoin_price")))
            matecoin_account += Decimal(transaction.get("bought"))

        if transaction.get("sold") is not None:
            earned_money += (Decimal(transaction.get("sold"))
                             * Decimal(transaction.get("matecoin_price")))
            matecoin_account -= Decimal(transaction.get("sold"))

    with open("profit.json", "w") as profit_file:
        json.dump({
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        },
            profit_file,
            indent=2
        )
