import json
from decimal import Decimal
from typing import List, Dict, Any


def calculate_profit(file_path: str) -> None:
    def read_json(file_path: str) -> List[Dict[str, Any]]:
        with open(file_path, "r") as file:
            return json.load(file)

    def write_json(data: Dict[str, str], file_path: str) -> None:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=2)

    trades = read_json(file_path)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
        if trade["sold"] is not None:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    write_json(result, "profit.json")
