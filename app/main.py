import json
from decimal import Decimal
import os


def calculate_profit(file_json: str) -> None:
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, file_json)

    with open(file_path, "r") as file:
        reader = json.load(file)

    money = 0
    matecoin = 0
    for info in reader:
        if info["bought"] is not None:
            matecoin += Decimal(info["bought"])
            money -= Decimal(info["matecoin_price"]) * Decimal(info["bought"])
        if info["sold"] is not None:
            matecoin -= Decimal(info["sold"])
            money += Decimal(info["matecoin_price"]) * Decimal(info["sold"])
    result = {
        "earned_money": str(money),
        "matecoin_account": str(matecoin)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
