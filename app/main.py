import json
from decimal import Decimal
from typing import List, Dict, Optional


def calculate_profit(trades_file_name: str) -> None:
    with open(trades_file_name, "r") as source_file:
        trades_data: List[Dict[str, Optional[str]]] = json.load(source_file)

    earned_money: Decimal = Decimal("0")
    matecoin_account: Decimal = Decimal("0")

    for trade in trades_data:
        current_price: Decimal = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_volume: Decimal = Decimal(trade["bought"])
            earned_money -= bought_volume * current_price
            matecoin_account += bought_volume

        if trade["sold"] is not None:
            sold_volume: Decimal = Decimal(trade["sold"])
            earned_money += sold_volume * current_price
            matecoin_account -= sold_volume

    result_data: Dict[str, str] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # Зміни тільки цей рядок у кінці функції
    with open("profit.json", "w") as result_file:
        json.dump(result_data, result_file, indent=2)
