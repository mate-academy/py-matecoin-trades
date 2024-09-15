import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        new_list = json.load(file)
        bought_account = decimal.Decimal("0")
        sold_account = decimal.Decimal("0")
        bought_price = decimal.Decimal("0")
        sold_price = decimal.Decimal("0")
        for info_dict in new_list:
            if info_dict.get("bought"):
                bought_price += (
                    decimal.Decimal(info_dict.get("bought"))
                    * decimal.Decimal(info_dict.get("matecoin_price"))
                )
                bought_account += decimal.Decimal(info_dict.get("bought"))
            if info_dict.get("sold"):
                sold_price += (
                    decimal.Decimal(info_dict.get("sold"))
                    * decimal.Decimal(info_dict.get("matecoin_price"))
                )
                sold_account += decimal.Decimal(info_dict.get("sold"))
        earned_money = sold_price - bought_price
        matecoin_account = bought_account - sold_account
        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        with open("profit.json", "w") as file_profit:
            json.dump(profit, file_profit, indent=2)
