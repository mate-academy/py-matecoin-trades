import json
import decimal
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROFIT = f"{BASE_DIR}/profit.json"


def calculate_profit(trades: str) -> None:
    with open(trades) as json_data:
        data = json.load(json_data)

    profit = 0
    matecoins = 0

    for item in data:
        spend = 0
        received = 0
        price = decimal.Decimal(item["matecoin_price"])
        if item["bought"] is not None:
            bought = decimal.Decimal(item["bought"])
            matecoins += bought
            spend = bought * price
        if item["sold"] is not None:
            sold = decimal.Decimal(item["sold"])
            matecoins -= sold
            received = sold * price
        profit += received - spend

    with open(PROFIT, "w") as f:
        json.dump(
            {
                "earned_money": str(profit),
                "matecoin_account": str(matecoins)
            },
            f, indent=2
        )
    return None
