import json
import decimal


def calculate_profit(json_file: str) -> None:
    with open(json_file, "r") as j_file:
        json_data = json.load(j_file)
        earned_money = 0
        matecoin_account = 0
        for record in json_data:
            if record.get("bought"):
                earned_money -= (
                    decimal.Decimal(record.get("matecoin_price"))
                    * decimal.Decimal(record.get("bought"))
                )
                matecoin_account += decimal.Decimal(record.get("bought"))
            if record.get("sold"):
                earned_money += (
                    decimal.Decimal(record.get("matecoin_price"))
                    * decimal.Decimal(record.get("sold"))
                )
                matecoin_account -= decimal.Decimal(record.get("sold"))

        dict_to_write = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        with open("profit.json", "w") as file_to_write:
            json.dump(dict_to_write, file_to_write, indent=2)
