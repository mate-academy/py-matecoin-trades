import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(name, "r") as f:
        trades = json.load(f)
        for tread in trades:
            if tread["bought"] is not None:
                matecoin_account += Decimal(f"{tread["bought"]}")
                earned_money -= Decimal(
                    f"{tread["bought"]}") * Decimal(f"{tread["matecoin_price"]}"
                )
            if tread["sold"] is not None:
                matecoin_account -= Decimal(f"{tread["sold"]}")
                earned_money += (
                        Decimal(f"{tread["sold"]}") * Decimal(f"{tread["matecoin_price"]}")
                )

    result_dict = {
        "earned_money": f"{earned_money}",
        "matecoin_account": f"{matecoin_account}"
    }

    with open("profit.json", "w") as file:
        json.dump(result_dict, file, indent=2)