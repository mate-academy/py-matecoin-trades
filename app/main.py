import json
import decimal
from typing import Any


def calculate_profit(file_name: Any) -> None:
    bought_in_dollars = 0
    sold_in_dollars = 0
    amount = 0
    with open(f"{file_name}") as file:
        trade_descriptions = json.load(file)
    for dict_of_trade in trade_descriptions:
        if dict_of_trade["bought"]:
            bought_in_dollars\
                += (decimal.Decimal(f"{dict_of_trade['bought']}")
                    * decimal.Decimal(f"{dict_of_trade['matecoin_price']}"))
            amount += decimal.Decimal(f"{dict_of_trade['bought']}")
        if dict_of_trade["sold"]:
            sold_in_dollars +=\
                (decimal.Decimal(f"{dict_of_trade['sold']}")
                 * decimal.Decimal(f"{dict_of_trade['matecoin_price']}"))
            amount -= decimal.Decimal(f"{dict_of_trade['sold']}")
    dict_of_profit = {
        "earned_money": str(sold_in_dollars - bought_in_dollars),
        "matecoin_account": str(amount)
    }
    with open("profit.json", "w") as file:
        json.dump(dict_of_profit, file, indent=4)
