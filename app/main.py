from decimal import Decimal
import json


def calculate_profit(
        file_name: str,) -> None:
    with open(file_name, "r") as file:
        file_data = json.load(file)
        print(file_data)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for dictionary in file_data:
        bought = Decimal(dictionary.get("bought") or "0")
        sold = Decimal(dictionary.get("sold") or "0")
        matecoin_price = Decimal(dictionary["matecoin_price"])

        earned_money += (sold - bought) * matecoin_price
        matecoin_account += bought - sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit:
        json.dump(result, profit, indent=2)



# calculate_profit("trades.json")
