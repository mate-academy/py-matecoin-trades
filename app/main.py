import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        loaded_file = json.load(f)
        earned_money = 0
        matecoin_account = 0
        for info in loaded_file:
            if info["bought"] is not None:
                earned_money -= decimal.Decimal(info["bought"]) * \
                    decimal.Decimal(info["matecoin_price"])
                matecoin_account += decimal.Decimal(info["bought"])
            if info["sold"] is not None:
                earned_money += decimal.Decimal(info["sold"]) * \
                    decimal.Decimal(info["matecoin_price"])
                matecoin_account -= decimal.Decimal(info["sold"])
        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        with open("profit.json", "w") as new_file:
            json.dump(result, new_file, indent=2)
