import json
import decimal
from typing import Dict, List, Optional


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades: List[Dict[str, Optional[str]]] = json.load(f)

    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    for trade in trades:
        bought = (
            decimal.Decimal(trade["bought"])
            if trade["bought"]
            else decimal.Decimal("0")
        )
        sold = (
            decimal.Decimal(trade["sold"])
            if trade["sold"]
            else decimal.Decimal("0")
        )
        matecoin_price = decimal.Decimal(trade["matecoin_price"])

    matecoin_account += bought - sold
    earned_money += sold * matecoin_price - bought * matecoin_price

    result: Dict[str, str] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=4)
