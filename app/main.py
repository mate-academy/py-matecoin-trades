import json
from decimal import Decimal


def calculate_profit(file_json_arg: str) -> None:
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    with open(file_json_arg, "r", encoding="utf-8") as json_file:
        file_json_on_py = json.load(json_file)

    for dict_py in file_json_on_py:

        if dict_py["bought"] is None:
            earned_money += (
                Decimal(dict_py["sold"])
                * Decimal(dict_py["matecoin_price"])
            )
            matecoin_account -= Decimal(dict_py["sold"])
        elif dict_py["sold"] is None:
            earned_money -= (
                Decimal(dict_py["bought"])
                * Decimal(dict_py["matecoin_price"])
            )
            matecoin_account += Decimal(dict_py["bought"])
        else:
            earned_money += (
                Decimal(dict_py["sold"])
                * Decimal(dict_py["matecoin_price"])
            )
            matecoin_account -= Decimal(dict_py["sold"])
            earned_money -= (
                Decimal(dict_py["bought"])
                * Decimal(dict_py["matecoin_price"])
            )
            matecoin_account += Decimal(dict_py["bought"])

    result_file = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w", encoding="utf-8") as profit:
        json.dump(result_file, profit, indent=2, ensure_ascii=False)
