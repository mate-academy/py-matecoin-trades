from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    earned_money = 0
    matecoin_account = 0
    with open(filename, "r") as input_file:
        json_trades = json.load(input_file)
    for el in json_trades:
        bought = Decimal(el.get("bought") or "0")
        sold = Decimal(el.get("sold") or "0")
        price = Decimal(el.get("matecoin_price"))
        earned_money += sold * price - bought * price
        matecoin_account += bought - sold
    data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as output_data:
        json.dump(data, output_data, indent=2)
