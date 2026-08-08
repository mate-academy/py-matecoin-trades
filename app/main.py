import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data_trades = json.load(file)

    matecoin = 0
    valet = 0
    for monetary_support in data_trades:
        # print(f"{monetary_support["bought"] = }")
        # print(f"{monetary_support["sold"] = }")
        if monetary_support["bought"]:
            valet -= Decimal(
                monetary_support[
                    "bought"
                ]
            ) * Decimal(
                monetary_support[
                    "matecoin_price"
                ]
            )
            matecoin += Decimal(monetary_support["bought"])
        if monetary_support["sold"]:
            valet += Decimal(
                monetary_support[
                    "sold"
                ]
            ) * Decimal(
                monetary_support[
                    "matecoin_price"
                ]
            )
            matecoin -= Decimal(monetary_support["sold"])

    profit = {"earned_money": str(valet),
              "matecoin_account": str(matecoin)}
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
