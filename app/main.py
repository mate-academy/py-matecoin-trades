import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as js_file:
        data = json.load(js_file)

    bought_pr = 0
    bought = 0
    sold_pr = 0
    sold = 0
    print(data)
    for trade in data:
        for key in trade:
            if key == "bought" and trade.get(key):
                bought_pr += (Decimal(trade.get(key, 0))
                              * Decimal(trade["matecoin_price"]))
                bought += Decimal(trade.get(key, 0))
            if key == "sold" and trade.get(key):
                sold_pr += (Decimal(trade.get(key, 0))
                            * Decimal(trade["matecoin_price"]))
                sold += Decimal(trade.get(key, 0))
    earned = str(sold_pr - bought_pr)
    account = str(bought - sold)
    res = {
        "earned_money": earned,
        "matecoin_account": account,
    }
    with open("profit.json", "a") as res_file:
        json.dump(res, res_file, indent=2)
