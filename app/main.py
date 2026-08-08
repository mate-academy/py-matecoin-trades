import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as js_data:
        data: list[dict] = json.load(js_data)

        earned_money = Decimal()
        matecoin_account = Decimal()

        for element in data:
            mate_coin = Decimal(element.get("matecoin_price"))
            bought = Decimal(element.get("bought") or 0)
            sold = Decimal(element.get("sold") or 0)
            different = sold * mate_coin - bought * mate_coin

            earned_money += different
            matecoin_account += bought - sold

    with open("profit.json", "w") as file_profit:
        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }
        json.dump(result, file_profit, indent=2)
