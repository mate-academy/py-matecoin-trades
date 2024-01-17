import decimal
import json


def calculate_profit(json_file_name: str) -> None:
    with open(json_file_name) as f:
        transaction_info = json.load(f)
        print(transaction_info)
        earned_money = 0
        matecoin_account = 0
        for data in transaction_info:
            if data["bought"] is not None:
                earned_money -= (decimal.Decimal(data["bought"])
                                 * decimal.Decimal(data["matecoin_price"]))
                matecoin_account += decimal.Decimal(data["bought"])
            if data["sold"] is not None:
                earned_money += (decimal.Decimal(data["sold"])
                                 * decimal.Decimal(data["matecoin_price"]))
                matecoin_account -= decimal.Decimal(data["sold"])
        info_to_write = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as file_to:
            json.dump(info_to_write, file_to, indent=2)
