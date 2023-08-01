import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file) as f:
        trades_data = json.load(f)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        if trade["sold"] is not None:
            earned_money += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            matecoin_account -= Decimal(trade["sold"])
        if trade["bought"] is not None:
            earned_money -= Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            matecoin_account += Decimal(trade["bought"])

    profit = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)

# calculate_profit("trades.json")

# [
#   {
#     "bought": "0.00085",
#     "sold": null,
#     "matecoin_price": "65980.63"
#   },
#   {
#     "bought": "0.00009",
#     "sold": null,
#     "matecoin_price": "65384.98"
#   },
#   {
#     "bought": "0.00011",
#     "sold": null,
#     "matecoin_price": "48911.23"
#   },
#   {
#     "bought": null,
#     "sold": "0.00058",
#     "matecoin_price": "77830.83"
#   },
#   {
#     "bought": "0.0013",
#     "sold": null,
#     "matecoin_price": "60340.78"
#   },
#   {
#     "bought": null,
#     "sold": "0.0003",
#     "matecoin_price": "93789.11"
#   },
#   {
#     "bought": "0.0007",
#     "sold": null,
#     "matecoin_price": "60340.55"
#   },
#   {
#     "bought": null,
#     "sold": "0.0021",
#     "matecoin_price": "78366.14"
#   }
# ]
