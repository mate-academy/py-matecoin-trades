import json
from decimal import Decimal
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def calculate_profit(filename: str) -> None:
    with open(filename) as f:
        coin_data = json.load(f)

    proper_coin_data = []
    for data in coin_data:
        make_dict_from_json = {
            k: Decimal(v)
            if v is not None else 0
            for k, v in data.items()
        }
        proper_coin_data.append(make_dict_from_json)

    sum_bought, sum_matecoin_account, sum_sold = 0, 0, 0
    for data in proper_coin_data:
        sum_bought += data["bought"]
        sum_matecoin_account += data["matecoin_price"]
        sum_sold += data["sold"]

    # bought = sum(data["bought"] for data in proper_coin_data)
    # sold = sum(data["sold"] for data in proper_coin_data)

    bought_amount = sum(
        data["bought"] * data["matecoin_price"]
        for data in proper_coin_data
    )
    sold_amount = sum(
        data["sold"] * data["matecoin_price"]
        for data in proper_coin_data
    )

    earned_money = sold_amount - bought_amount
    matecoin_account = sum_bought - sum_sold

    res_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open(f"{BASE_DIR}/profit.json", "w") as f:
        json.dump(res_dict, f, indent=2)
