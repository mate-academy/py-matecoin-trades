from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    with open(filename) as json_file:
        trades = json.load(json_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = trade["bought"]
        sold = trade["sold"]
        matecoin_price = trade["matecoin_price"]

        if bought is not None:
            bought = Decimal(bought)
            matecoin_price = Decimal(matecoin_price)
            cost = bought * matecoin_price
            earned_money = earned_money - cost
            matecoin_account = matecoin_account + bought

        if sold is not None:
            sold = Decimal(sold)
            matecoin_price = Decimal(matecoin_price)
            revenue = sold * matecoin_price
            earned_money = earned_money + revenue
            matecoin_account = matecoin_account - sold

    result = {}
    result["earned_money"] = str(earned_money)
    result["matecoin_account"] = str(matecoin_account)

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
