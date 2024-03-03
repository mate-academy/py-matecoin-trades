import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:

    with open(trades_file) as data:
        deals = json.load(data)

    profit = 0
    coins_amount = 0

    for deal in deals:
        if deal["bought"]:
            deal_amount = Decimal(deal["bought"])
            profit -= (deal_amount * Decimal(deal["matecoin_price"]))
            coins_amount += deal_amount

        if deal["sold"]:
            deal_amount = Decimal(deal["sold"])
            profit += (deal_amount * Decimal(deal["matecoin_price"]))
            coins_amount -= deal_amount

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(coins_amount)
    }

    with open("profit.json", "w") as output:
        json.dump(result, output, indent=2)
