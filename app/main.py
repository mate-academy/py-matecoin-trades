import json
import decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file, "r") as json_file:
        data = json.load(json_file)

    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    for item in data:
        if item.get("bought") is not None:
            bought_coins = decimal.Decimal(item["bought"])
            mate_coins = decimal.Decimal(item["matecoin_price"])

            matecoin_account += bought_coins

            spent_dollars = mate_coins * bought_coins
            earned_money -= spent_dollars

        if item.get("sold") is not None:
            sold_coins = decimal.Decimal(item["sold"])
            mate_coins = decimal.Decimal(item["matecoin_price"])

            matecoin_account -= sold_coins
            earned_dollars = mate_coins * sold_coins
            earned_money += earned_dollars
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as json_file:
        json.dump(result, json_file, indent=2)
