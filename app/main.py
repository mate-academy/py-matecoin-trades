from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    deals = {}

    with open(file_name, "r") as deals_file:
        deals = json.load(deals_file)

    profit = Decimal("0")
    matecoin = Decimal("0")

    for deal in deals:
        if deal["bought"] is not None:
            profit -= (Decimal(deal["bought"])
                       * Decimal(deal["matecoin_price"]))
            matecoin += Decimal(deal["bought"])

        if deal["sold"] is not None:
            profit += Decimal(deal["sold"]) * Decimal(deal["matecoin_price"])
            matecoin -= Decimal(deal["sold"])

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin)
    }

    with open("profit.json", "w") as output_file:
        json.dump(result, output_file, indent=2)
