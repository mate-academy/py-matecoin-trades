import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        users_data = json.load(file)

        sum_of_bought = Decimal("0")
        sum_of_sold = Decimal("0")
        matecoin_account = Decimal("0")

    for user in users_data:
        if user["bought"]:
            sum_of_bought += (Decimal(user["bought"])
                              * Decimal(user["matecoin_price"]))
            matecoin_account += Decimal(user["bought"])
        if user["sold"]:
            sum_of_sold += (Decimal(user["sold"])
                            * Decimal(user["matecoin_price"]))
            matecoin_account -= Decimal(user["sold"])

    profit = {
        "earned money": str(sum_of_sold - sum_of_bought),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as result:
        json.dump(profit, result, indent=2)
