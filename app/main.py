import json
from decimal import Decimal

def calculate_profit(file_name: str) -> None :

    with open(file_name, "r") as file:
        traders_data = json.load(file)

    earned_money = Decimal(0)
    metacoin_account = Decimal(0)

    for day in traders_data:
        if day["bought"] is not None:
            bought = day["bought"]
            earned_money -= Decimal(day["matecoin_price"]) * Decimal(day["bought"])
            metacoin_account += Decimal(bought)
        if day["sold"] is not None:
            sold = day["sold"]
            earned_money += Decimal(day["matecoin_price"]) * Decimal(day["sold"])
            metacoin_account -= Decimal(sold)

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(metacoin_account)
    }


    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)

