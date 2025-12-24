from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    total_bought, total_coins = Decimal("0.0"), Decimal("0.0")
    total_sold, total_sold_coins = Decimal("0.0"), Decimal("0.0")
    result_dict = {}

    with open(file_name, "r") as f:
        data_read = json.load(f)
        print(data_read)

    for i in data_read:

        if i["bought"] is not None:
            total_bought += Decimal(i["bought"]) * Decimal(i["matecoin_price"])
            total_coins += Decimal(i["bought"])
        if i["sold"] is not None:
            total_sold += Decimal(i["sold"]) * Decimal(i["matecoin_price"])
            total_sold_coins += Decimal(i["sold"])

    result_dict["earned_money"] = str((total_bought - total_sold) * (-1))
    result_dict["matecoin_account"] = str(total_coins - total_sold_coins)

    with open("profit.json", "w") as fw:
        json.dump(result_dict, fw, indent=2)
