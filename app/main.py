import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        trades = json.load(json_file)

    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    for trade in trades:
        if trade["bought"]:
            bought_volume = decimal.Decimal(trade["bought"])
            price = decimal.Decimal(trade["matecoin_price"])
            matecoin_account += bought_volume
            earned_money -= bought_volume * price

        if trade["sold"]:
            sold_volume = decimal.Decimal(trade["sold"])
            price = decimal.Decimal(trade["matecoin_price"])
            matecoin_account -= sold_volume
            earned_money += sold_volume * price

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }

        with open("profit.json", "w") as file:
            json.dump(result, file, indent=2)
