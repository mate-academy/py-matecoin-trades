import json
from decimal import Decimal


result = {"earned_money": Decimal("0"), "matecoin_account": Decimal("0")}
with open("trades.json", "r") as f:
    wallet = json.load(f)
for coin in wallet:
    if coin["bought"] is not None:
        result["earned_money"] -= Decimal(coin["bought"]) * Decimal(coin["matecoin_price"])
        result["matecoin_account"] += Decimal(coin["bought"])
    if coin["sold"] is not None:
        result["earned_money"] += Decimal(coin["sold"]) * Decimal(coin["matecoin_price"])
        result["matecoin_account"] -= Decimal(coin["sold"])
earned = result["earned_money"]
balance = result["matecoin_account"]
result = {"earned_money": str(earned), "matecoin_account": str(balance)}


with open("profit.json", "w") as file:
    json.dump(result, file)
