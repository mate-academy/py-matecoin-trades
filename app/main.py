import json
from decimal import Decimal


def calculate_profit(trades_file_name: str) -> None:
    with open(trades_file_name) as f:
        result_of_trade = json.load(f)

    matecoin_account = Decimal("0")
    if_buy_money = Decimal("0")
    if_sold_money = Decimal("0")

    for data_about_trade in result_of_trade:
        if data_about_trade["bought"] is not None:
            matecoin_account += Decimal(data_about_trade["bought"])
            if_buy_money += (Decimal(data_about_trade["bought"])
                             * Decimal(data_about_trade["matecoin_price"]))
        if data_about_trade["sold"] is not None:
            matecoin_account -= Decimal(data_about_trade["sold"])
            if_sold_money += (Decimal(data_about_trade["sold"])
                              * Decimal(data_about_trade["matecoin_price"]))

    earned_money = if_sold_money - if_buy_money

    my_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(my_dict, f, indent=2)
