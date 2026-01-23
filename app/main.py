import json
from decimal import Decimal
#
#
# def calculate_profit(trades: str) -> None:
#     earned_money = Decimal("0")
#     matecoin_account = Decimal("0")
#     with open(trades, "r") as f:
#         data = json.load(f)
#     for trade in data:
#         if trade["bought"] is None:
#             if trade["sold"]:
#                 earned_money +=\
#                     Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
#                 matecoin_account -= Decimal(trade["sold"])
#         else:
#             if trade["bought"]:
#                 earned_money -=\
#                     Decimal(trade["bought"])
#                     * Decimal(trade["matecoin_price"])
#                 matecoin_account += Decimal(trade["bought"])
#     result = {
#         "earned_money": str(earned_money),
#         "matecoin_account": str(matecoin_account),
#     }
#     with open("profit.json", "w") as file:
#         json.dump(result, file, indent=2)


def calculate_profit(trades: str) -> dict:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(trades, "r") as f:
        data = json.load(f)

    for trade in data:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_amount = Decimal(trade["bought"])
            earned_money -= bought_amount * matecoin_price
            matecoin_account += bought_amount

        if trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            earned_money += sold_amount * matecoin_price
            matecoin_account -= sold_amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
