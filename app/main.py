import json
import decimal


profit = 0
result = {
    "earned_money": 0,
    "matecoin_account": "0.00053"
}

with open("trades.json", "r") as file:
    money = json.load(file)

for day in money:
    if day["bought"] is not None:
        total_bought = decimal.Decimal(day["bought"])
        bought_price = decimal.Decimal(day["matecoin_price"])
        profit -= total_bought * bought_price
    else:
        total_sold = decimal.Decimal(day["sold"])
        sold_price = decimal.Decimal(day["matecoin_price"])
        profit += total_sold * sold_price


result["earned_money"] = str(profit)

with open("profit.json", "w") as f:
    json.dump(result, f, indent=2)
