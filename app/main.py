from decimal import Decimal
import json


def calculate_profit(path_to_file: str) -> None:
    with (open(path_to_file, "r") as file):
        new_dict = json.load(file)
        earned_money = Decimal("0")
        matecoin_account = Decimal("0")
        for el in new_dict:
            if el["bought"] is not None:
                matecoin_account += Decimal(el["bought"])
                earned_money -= Decimal(el["bought"]
                                        ) * Decimal(el["matecoin_price"])
            if el["sold"] is not None:
                matecoin_account -= Decimal(el["sold"])
                earned_money += Decimal(el["sold"]
                                        ) * Decimal(el["matecoin_price"])

        result = {"earned_money": str(earned_money),
                  "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)


calculate_profit("app/trades.json")
