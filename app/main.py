# import os
# import json
# from decimal import Decimal
#
#
# def calculate_profit(file_name: str) -> None:
#     try:
#         with open(file_name, "r") as file:
#             trades = json.load(file)
#     except (FileNotFoundError, json.JSONDecodeError):
#         print("Error: Unable to open or read json file.")
#         return
#
#     matecoin = Decimal("0")
#     cash = Decimal("0")
#
#     for trade in trades:
#         bought = Decimal(trade["bought"]) \
#             if trade.get("bought") is not None else Decimal("0")
#         sold = Decimal(trade["sold"]) \
#             if trade.get("sold") is not None else Decimal("0")
#         price = Decimal(trade["matecoin_price"]) \
#             if trade.get("matecoin_price") is not None else Decimal("0")
#
#         if bought > 0:
#             matecoin += bought
#             cash -= bought * price
#
#         if sold > 0:
#             matecoin -= sold
#             cash += sold * price
#
#     output_file = os.path.join(
#         os.path.dirname(
#             os.path.abspath(__file__)
#         ), "..", "profit.json"
#     )
#     try:
#         with open(output_file, "w") as outfile:
#             json.dump(
#                 {
#                     "earned_money": str(cash),
#                     "matecoin_account": str(matecoin),
#                 },
#                 outfile,
#                 indent=2,
#             )
#     except IOError:
#         print("Error writing to profit.json file")


import os
import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    try:
        with open(file_name, "r") as file:
            trades = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: Unable to open or read json file.")
        return

    matecoin, cash = Decimal("0"), Decimal("0")

    for trade in trades:
        bought = Decimal(trade.get("bought", "0") or "0")
        sold = Decimal(trade.get("sold", "0") or "0")
        price = Decimal(trade.get("matecoin_price", "0"))

        matecoin += bought - sold
        cash += sold * price - bought * price

    output_file = os.path.join(os.path.dirname(__file__), "..", "profit.json")
    try:
        with open(output_file, "w") as outfile:
            json.dump(
                {"earned_money": str(cash), "matecoin_account": str(matecoin)},
                outfile,
                indent=2,
            )
    except IOError:
        print("Error writing to profit.json file")
