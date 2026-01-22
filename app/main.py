import json
from decimal import Decimal


def calculate_profit(trade_info: str) -> None:
    deals = []

    with open(trade_info) as data:
        deals = json.load(data)

    profit = 0
    coins_amount = 0

    for deal in deals:
        if deal["bought"]:
            deal_amount = Decimal(str(deal["bought"]))
            profit -= (deal_amount * Decimal(str(deal["matecoin_price"])))
            coins_amount += deal_amount
        if deal["sold"]:
            deal_amount = Decimal(str(deal["sold"]))
            profit += (deal_amount * Decimal(str(deal["matecoin_price"])))
            coins_amount -= deal_amount

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(coins_amount)
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
