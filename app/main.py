import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    bought = Decimal(0.0)
    sold = Decimal(0.0)
    matecoin_account = Decimal(0.0)
    with open(file_name, "r") as f:
        trades = json.load(f)
    for index, trade in enumerate(trades):
        if trades[index]["bought"]:
            bought += Decimal(
                trades[index]["bought"]
            ) * Decimal(trades[index]["matecoin_price"]
                        )
            matecoin_account += Decimal(
                trades[index]["bought"]
            )
        if trades[index]["sold"]:
            sold += Decimal(
                trades[index]["sold"]
            ) * Decimal(trades[index]["matecoin_price"]
                        )
            matecoin_account -= Decimal(trades[index]["sold"])
    profits = {
        "earned_money": f"{sold - bought}",
        "matecoin_account": f"{matecoin_account}"
    }
    with open("profit.json", "w") as f:
        json.dump(profits, f, indent=2)
