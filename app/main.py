import json
from decimal import Decimal


def calculate_profit(trades_json: str) -> None:
    with open(trades_json) as f:
        list_operation = json.load(f)

    matecoin_account = Decimal("0.0")
    matecoin_price = Decimal("0.0")

    for i in list_operation:
        if i["bought"] is not None:
            matecoin_account += Decimal(i["bought"])
            matecoin_price -= (Decimal(i["bought"])) * \
                              (Decimal(i["matecoin_price"]))
        if i["sold"] is not None:
            matecoin_account -= Decimal(i["sold"])
            matecoin_price += (Decimal(i["sold"])) * \
                              (Decimal(i["matecoin_price"]))

    result = ({"earned_money": str(matecoin_price),
               "matecoin_account": str(matecoin_account)})

    with open("profit.json", "w") as k:
        json.dump(result, k, indent=2)
