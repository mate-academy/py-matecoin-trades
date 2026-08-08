import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as file:
        trades = json.load(file)

    bought = 0
    sold = 0
    spent = 0
    earned = 0
    for el in trades:
        if el["bought"] is not None:
            bought += Decimal(el["bought"])
            spent += Decimal(el["bought"]) * Decimal(el["matecoin_price"])

        if el["sold"] is not None:
            sold += Decimal(el["sold"])
            earned += Decimal(el["sold"]) * Decimal(el["matecoin_price"])

    matecoin_account = bought - sold
    earned_money = earned - spent

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)

    print(result)
