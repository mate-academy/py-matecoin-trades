from decimal import Decimal
import json


def calculate_profit(trades_file_path: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(trades_file_path, "r") as f:
        trades = json.load(f)

    for data in trades:
        if data["bought"] is not None:
            earned_money -= (Decimal(data["bought"])
                             * Decimal(data["matecoin_price"]))

            matecoin_account += Decimal((data["bought"]))

        if data["sold"] is not None:
            earned_money += (Decimal(data["sold"])
                             * Decimal(data["matecoin_price"]))

            matecoin_account -= Decimal(data["sold"])

    with open("profit.json", "w") as f:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account),
            },
            f,
            indent=2
        )
