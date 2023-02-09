from decimal import Decimal
import json


def calculate_profit(file_name: str):
    with (open(file_name) as data_from_json,
          open("profit.json", "w") as data_to_json):
        json_data = json.load(data_from_json)
        earned_money = 0
        matecoin_account = 0
        for i in json_data:
            for key, value in i.items():
                if key == "bought" and value is not None:
                    earned_money -= (Decimal(value)
                                     * Decimal(i["matecoin_price"]))
                    matecoin_account += Decimal(value)
                elif key == "sold" and value is not None:
                    earned_money += (Decimal(value)
                                     * Decimal(i["matecoin_price"]))
                    matecoin_account -= Decimal(value)
        coin_trade = {
            "earned_money": f"{earned_money}",
            "matecoin_account": f"{matecoin_account}"
        }
        json.dump(coin_trade, data_to_json, indent=2)
