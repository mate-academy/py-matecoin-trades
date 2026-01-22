import json
from decimal import Decimal


def calculate_profit(file_name: str):
    with open(file_name) as f:
        file_info = json.load(f)

        sold_in_dollars = 0
        bought_in_dollars = 0
        matecoin_account = 0

        for one_day in file_info:
            # sold = Decimal(one_day["sold"])
            # bought = Decimal(one_day["bought"])
            matecoin_price = Decimal(one_day["matecoin_price"])

            if one_day["bought"] is None:

                sold = Decimal(one_day["sold"])

                sold_in_dollars += sold * matecoin_price
                matecoin_account -= sold
            elif one_day["sold"] is None:

                bought = Decimal(one_day["bought"])

                bought_in_dollars += bought * matecoin_price
                matecoin_account += bought
            else:

                sold = Decimal(one_day["sold"])
                bought = Decimal(one_day["bought"])

                sold_in_dollars += sold * matecoin_price
                matecoin_account -= sold
                bought_in_dollars += bought * matecoin_price
                matecoin_account += bought

        new_jf_info = {
            "earned_money": f"{sold_in_dollars - bought_in_dollars}",
            "matecoin_account": f"{matecoin_account}"
        }

    with open("profit.json", "w") as jf:
        json.dump(new_jf_info, jf, indent=2)
