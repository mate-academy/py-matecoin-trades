from decimal import Decimal
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROFIT = f"{BASE_DIR}/profit.json"


def calculate_profit(file_transact: str) -> None:
    matecoin_account = 0
    earned_money = 0
    with open(file_transact) as data_transact:
        history_coin = json.load(data_transact)
        for one in history_coin:
            if one["bought"] is not None:
                bouth = Decimal(one["bought"]) * Decimal(one["matecoin_price"])
                matecoin_account += Decimal(one["bought"])
                earned_money -= bouth
            if one["sold"] is not None:
                sold = Decimal(one["sold"]) * Decimal(one["matecoin_price"])
                matecoin_account -= Decimal(one["sold"])
                earned_money += sold

    with open(PROFIT, "w") as json_file:
        json.dump({
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }, json_file, indent=2)
