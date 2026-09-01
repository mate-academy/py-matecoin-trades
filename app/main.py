import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    total_bought = Decimal("0")
    total_sold = Decimal("0")
    total_earned = Decimal("0")
    total_spent = Decimal("0")

    print(name)
    with open(name, "r") as f:
        user_data = json.load(f)

    for data in user_data:
        if data["sold"]:
            total_earned += (Decimal(data["sold"])
                             * Decimal(data["matecoin_price"]))
            total_sold += Decimal(data["sold"])
        if data["bought"]:
            total_spent += (Decimal(data["bought"])
                            * Decimal(data["matecoin_price"]))
            total_bought += Decimal(data["bought"])

    profit = total_earned - total_spent
    matecoin_account = total_bought - total_sold
    result_data = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as f:
        json.dump(result_data, f, indent=2)
