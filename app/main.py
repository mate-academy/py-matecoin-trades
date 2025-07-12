import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        result = json.load(f)

    bought_sum = 0
    sold_sum = 0
    sold_price_sum = 0
    bought_price_sum = 0

    for operation in result:
        if operation["bought"] is not None:
            bought_sum += Decimal(operation["bought"])
            bought_price_sum += (Decimal(operation["bought"])
                                 * Decimal(operation["matecoin_price"])
                                 )
        if operation["sold"] is not None:
            sold_sum += Decimal(operation["sold"])
            sold_price_sum += (Decimal(operation["sold"])
                               * Decimal(operation["matecoin_price"])
                               )

    matecoin_account = f"{bought_sum - sold_sum}"
    earned_money = f"{sold_price_sum - bought_price_sum}"
    result_operation = {
        "earned_money": earned_money,
        "matecoin_account": matecoin_account
    }

    with open("./profit.json", "w") as f:
        json.dump(result_operation, f, indent=2)
