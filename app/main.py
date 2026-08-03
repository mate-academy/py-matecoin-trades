import json
from decimal import Decimal


filename = "trades.json"


def calculate_profit(filename: str) -> None:
    with open(filename) as f:
        data = json.load(f)
    total_buy = Decimal("0")
    money_buy = Decimal("0")
    total_sold = Decimal("0")
    money_sold = Decimal("0")
    for elem in data:
        if elem["bought"]:
            total_buy += Decimal(elem["bought"])
            money_buy += (Decimal(elem["bought"])
                          * Decimal(elem["matecoin_price"]))
        if elem["sold"]:
            total_sold += Decimal(elem["sold"])
            money_sold += (Decimal(elem["sold"])
                           * Decimal(elem["matecoin_price"]))
    matecoin_account = total_buy - total_sold
    earned_money = money_sold - money_buy
    output_data = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as file:
        json.dump(output_data, file, indent=2)
