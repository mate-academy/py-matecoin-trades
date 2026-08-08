import decimal
import json


def calculate_profit(json_file: json) -> None:
    with open(json_file, "r") as filee:
        trades_list = json.load(filee)

    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    for trade in trades_list:
        if trade["bought"]:
            boughted_tokens = decimal.Decimal(trade["bought"])
            price_matecoin = decimal.Decimal(trade["matecoin_price"])
            earned_money -= price_matecoin * boughted_tokens
            matecoin_account += boughted_tokens

        if trade["sold"]:
            selled_tokens = decimal.Decimal(trade["sold"])
            price_matecoin = decimal.Decimal(trade["matecoin_price"])
            earned_money += price_matecoin * selled_tokens
            matecoin_account -= selled_tokens

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as new_file:
        json.dump(result, new_file, indent=2)
