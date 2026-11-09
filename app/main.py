import json
import decimal


def calculate_profit(story_data: str) -> None:
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    with open(story_data, "r") as file:
        data = json.load(file)

    for trade in data:
        price = decimal.Decimal(trade["matecoin_price"])

        if trade.get("bought") is not None:
            bought_amount = decimal.Decimal(trade["bought"])
            matecoin_account += bought_amount
            earned_money -= price * bought_amount

        if trade.get("sold") is not None:
            sold_amount = decimal.Decimal(trade["sold"])
            matecoin_account -= sold_amount
            earned_money += price * sold_amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as outfile:
        json.dump(result, outfile, indent=2)
