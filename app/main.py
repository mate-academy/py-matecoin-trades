from decimal import Decimal
import json


def calculate_profit(trades_path: str) -> None:
    from pathlib import Path

    trades_file = Path(trades_path)
    with trades_file.open() as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= Decimal(trade["bought"]) * matecoin_price
        if trade["sold"]:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += Decimal(trade["sold"]) * matecoin_price

    result = {
        "earned_money" : f"{earned_money: .7f}",
        "matecoin_account" : f"{matecoin_account: .5f}",
    }

    profit_file = trades_file.parent / "profit.json"
    with profit_file.open("w") as file:
        json.dump(result, file, indent=2)

    return None
