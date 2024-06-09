import json
import decimal


def calculate_profit(trades: str) -> None:
    some_dict = {
        "earned_money": "",
        "matecoin_account": ""
    }
    bought = 0
    sold = 0
    total_bought_value = 0
    total_sold_value = 0
    with open(trades, "r") as file:
        history = json.load(file)

    for deal in history:
        if deal["bought"] is not None:
            bought += decimal.Decimal(deal["bought"])
            total_bought_value += (
                decimal.Decimal(
                    deal["bought"]) * decimal.Decimal(deal["matecoin_price"])
            )
        if deal["sold"] is not None:
            sold += decimal.Decimal(deal["sold"])
            total_sold_value += (
                decimal.Decimal(
                    deal["sold"]) * decimal.Decimal(deal["matecoin_price"])
            )

    earned_money = total_sold_value - total_bought_value
    account = decimal.Decimal(bought) - decimal.Decimal(sold)
    some_dict["earned_money"] = str(earned_money)
    some_dict["matecoin_account"] = str(account)

    with open("profit.json", "w") as file:
        json.dump(some_dict, file, indent=2)
