import json
from decimal import Decimal


def calculate_profit(trades_path: str) -> None:
    with open(trades_path) as file:
        trades = json.load(file)
    earned_money = Decimal()
    matecoin_account = Decimal()
    for info in trades:
        info["matecoin_price"] = Decimal(info["matecoin_price"])
        if info["bought"] is not None:
            info["bought"] = Decimal(info["bought"])
            matecoin_account += info["bought"]
            earned_money -= info["bought"] * info["matecoin_price"]
        if info["sold"] is not None:
            info["sold"] = Decimal(info["sold"])
            matecoin_account -= info["sold"]
            earned_money += info["sold"] * info["matecoin_price"]
    with open("profit.json", "w") as file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            file,
            indent=2
        )
