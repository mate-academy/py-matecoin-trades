import json
from decimal import Decimal


def calculate_profit(market: json) -> json:
    with open(market) as f:
        market_data = json.load(f)
    profit = 0
    mate_coin = 0
    for day in market_data:
        if day["bought"] is not None:
            count = Decimal(day["bought"])
            price = Decimal(day["matecoin_price"])
            profit -= count * price
            mate_coin += count
        if day["sold"] is not None:
            count = Decimal(day["sold"])
            price = Decimal(day["matecoin_price"])
            profit += count * price
            mate_coin -= count
    result = {
        "earned_money": f"{profit}",
        "matecoin_account": f"{mate_coin}"
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
