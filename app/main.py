import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(filename: str) -> None:

    input_path = Path(filename).resolve()
    project_root = input_path.parent.parent
    output_path = project_root / "profit.json"

    with open(input_path, "r", encoding="utf-8") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade.get("bought"):
            bought_amount = Decimal(trade["bought"])
            earned_money -= bought_amount * matecoin_price
            matecoin_account += bought_amount

        if trade.get("sold"):
            sold_amount = Decimal(trade["sold"])
            earned_money += sold_amount * matecoin_price
            matecoin_account -= sold_amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)

    print(f"Profit file saved at: {output_path}")
