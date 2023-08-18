import json
from decimal import Decimal
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
PROFIT = f"{BASE_DIR}/profit.json"
print(PROFIT)


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as trade:
        trade_info_list = json.load(trade)

    matecoin_account = 0
    earned_money = 0
    for trade_info in trade_info_list:
        matecoin_price = Decimal(trade_info["matecoin_price"])
        if trade_info["bought"]:
            bought = Decimal(trade_info["bought"])
            matecoin_account += bought
            earned_money -= bought * matecoin_price

        if trade_info["sold"]:
            sold = Decimal(trade_info["sold"])
            matecoin_account -= sold
            earned_money += sold * matecoin_price

    with open(PROFIT, "w") as profit:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            profit,
            indent=2
        )
