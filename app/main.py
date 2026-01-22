import json
import decimal


def calculate_profit(trades: str):
    profit = 0
    account = 0
    result = {
        "earned_money": 0,
        "matecoin_account": "0.00053",
    }

    with open(trades, "r") as file:
        money = json.load(file)

    for day in money:
        if isinstance(day["bought"], str):
            total_bought = decimal.Decimal(day["bought"])
            bought_price = decimal.Decimal(day["matecoin_price"])
            profit -= total_bought * bought_price
            account += decimal.Decimal(day["bought"])
        if isinstance(day["sold"], str):
            total_sold = decimal.Decimal(day["sold"])
            sold_price = decimal.Decimal(day["matecoin_price"])
            profit += total_sold * sold_price
            account -= decimal.Decimal(day["sold"])

    result["earned_money"] = str(profit)
    result["matecoin_account"] = str(account)

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
