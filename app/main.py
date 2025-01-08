import json
from decimal import Decimal

trades = {}
profit = {"earned_money": "0",
          "matecoin_account": "0",
          }
with open("trades.json", "r") as file:
    trades = json.load(file)
for trade in trades:
    if trade["bought"]:
        profit["matecoin_account"] = str(Decimal(profit["matecoin_account"])
                                         - Decimal(trade["bought"]))
        profit["earned_money"] = str(Decimal(profit["earned_money"])
                                     - Decimal(trade["bought"])
                                     * Decimal(trade["matecoin_price"]))
    else:
        profit["matecoin_account"] = str(Decimal(profit["matecoin_account"])
                                         - Decimal(trade["sold"]))
        profit["earned_money"] = str(Decimal(profit["earned_money"])
                                     + Decimal(trade["sold"])
                                     * Decimal(trade["matecoin_price"]))

with open("profit.json", "w") as f:
    json.dump(profit, f, indent=2)
