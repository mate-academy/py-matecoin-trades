import json
import decimal
from pathlib import Path, PurePath

BASE_DIR = Path(__file__).resolve().parent.parent

def calculate_profit(json_file: str) -> None:
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")
    with open(json_file, "r") as f:
        trades_info = json.load(f)

    for trade in trades_info:
        if trade["bought"]:
            matecoin_account += decimal.Decimal(trade["bought"])
            earned_money -= decimal.Decimal(trade["bought"]) * decimal.Decimal(trade["matecoin_price"])

        if trade["sold"]:
            matecoin_account -= decimal.Decimal(trade["sold"])
            earned_money += decimal.Decimal(trade["sold"]) * decimal.Decimal(trade["matecoin_price"])

    with open(PurePath.joinpath(BASE_DIR, "profit.json"), "w") as f:
        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(result, f, indent=2)
