from decimal import Decimal
import json


def calculate_profit(file_name: str):
    with open(file_name, "r") as f:
        trade_list = json.load(f)

    matecoin = 0
    total_money = 0

    for deal in trade_list:
        try:
            if deal["bought"]:
                total_money -= (Decimal(deal["bought"]) * Decimal(
                    deal["matecoin_price"]))
                matecoin += Decimal(deal["bought"])
            if deal["sold"]:
                total_money += (Decimal(deal["sold"]) * Decimal(
                    deal["matecoin_price"]))
                matecoin -= Decimal(deal["sold"])
        except TypeError:
            continue

    with open("profit.json", 'w') as f:
        json.dump({"earned_money": str(total_money),
                   "matecoin_account": str(matecoin)}, f, indent=2)
