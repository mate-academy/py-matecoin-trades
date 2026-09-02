from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name) as work_file:
        data = json.load(work_file)

    total_earn = Decimal("0")
    total_coin = Decimal("0")

    for trade in data:
        if trade["bought"] is not None:
            total_earn -= (
                Decimal(trade["bought"])
                * Decimal(trade["matecoin_price"])
            )
            total_coin += Decimal(trade["bought"])
        if trade["sold"] is not None:
            total_earn += (
                Decimal(trade["sold"])
                * Decimal(trade["matecoin_price"])
            )
            total_coin -= Decimal(trade["sold"])

    result = {
        "earned_money": str(total_earn),
        "matecoin_account": str(total_coin)
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
