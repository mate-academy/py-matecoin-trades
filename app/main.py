from decimal import Decimal
import json


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as json_file:
        json_list = json.load(json_file)
        earned_money = 0
        matecoin_account = 0
        result_dict = {}
        for action in json_list:
            if action["bought"] and action["sold"]:
                earned_money -= (Decimal(action["bought"])
                                 * Decimal(action["matecoin_price"]))
                earned_money += (Decimal(action["sold"])
                                 * Decimal(action["matecoin_price"]))
                matecoin_account += Decimal(action["bought"])
                matecoin_account -= Decimal(action["sold"])
            elif action["bought"]:
                earned_money -= (Decimal(action["bought"])
                                 * Decimal(action["matecoin_price"]))
                matecoin_account += Decimal(action["bought"])
            else:
                earned_money += (Decimal(action["sold"])
                                 * Decimal(action["matecoin_price"]))
                matecoin_account -= Decimal(action["sold"])
        result_dict["earned_money"] = str(earned_money)
        result_dict["matecoin_account"] = str(matecoin_account)

        with open("profit.json", "w") as result_file:
            json.dump(result_dict, result_file, indent=2)
