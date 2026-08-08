import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(file_name: str) -> None:
    base_dir = Path(__file__).resolve().parent.parent
    profit_file = base_dir / "profit.json"
    with open(file_name) as file:
        trades = json.load(file)
    cost = Decimal("0")
    revenue = Decimal("0")
    account_bought = Decimal("0")
    account_sold = Decimal("0")
    for record in trades:
        if record.get("bought"):
            cost += (Decimal(record.get("bought"))
                     * Decimal(record.get("matecoin_price")))
            account_bought += Decimal(record.get("bought"))
        if record.get("sold"):
            revenue += (Decimal(record.get("sold"))
                        * Decimal(record.get("matecoin_price")))
            account_sold += Decimal(record.get("sold"))
    profit = {"earned_money": str(revenue - cost),
              "matecoin_account": str(account_bought - account_sold)}
    with profit_file.open("w") as new_file:
        json.dump(profit, new_file, indent=2)
