import json
from decimal import Decimal as d


def calculate_profit(file: str):
    with open(file) as f:
        data = json.load(f)

    sold = d("0")
    bought = d("0")
    sold_matecoin_price = d("0")
    bought_matecoin_price = d("0")

    for i in data:
        if not i["bought"]:
            sold += d(i["sold"])
            sold_matecoin_price += d(i["sold"]) * d(i["matecoin_price"])
        if not i["sold"]:
            bought += d(i["bought"])
            bought_matecoin_price += d(i["bought"]) * d(i["matecoin_price"])

    result = {
        "earned_money": str(sold_matecoin_price - bought_matecoin_price),
        "matecoin_account": str(bought - sold)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file, indent=2)
