import json
from decimal import Decimal


def calculate_profit(name_of_file: str) -> None:
    with open(name_of_file) as file_data, open("profit.json", "w") as new_file:
        data = json.load(file_data)

        bought = []
        sold = []

        for i in data:
            if i["bought"] is not None:
                bought.append({
                    "bought": i["bought"],
                    "matecoin_price": i["matecoin_price"]
                })
            if i["sold"] is not None:
                sold.append({
                    "sold": i["sold"],
                    "matecoin_price": i["matecoin_price"]
                })

        money_spent = Decimal("0")
        crypto = Decimal("0")
        for i in bought:
            crypto += Decimal(i["bought"])
            money_spent += Decimal(i["bought"]) * Decimal(i["matecoin_price"])

        crypto_sold = Decimal("0")
        money_gained = Decimal("0")
        for i in sold:
            crypto_sold += Decimal(i["sold"])
            money_gained += Decimal(i["sold"]) * Decimal(i["matecoin_price"])

        final_dict = {
            "earned_money": str(money_gained - money_spent),
            "matecoin_account": str(crypto - crypto_sold)
        }

        json.dump(final_dict, new_file, indent=2)
