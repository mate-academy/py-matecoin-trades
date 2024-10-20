import json
from decimal import Decimal


def calculate_profit(name_file: json) -> None:
    amount_matecoin = 0
    profit = 0
    with open(name_file, "r") as trades_file:
        count_date = json.load(trades_file)
        for transaction in count_date:
            if transaction["bought"] is not None:
                amount_matecoin += Decimal(f"{transaction["bought"]}")
                profit -= (
                    Decimal(f"{transaction["bought"]}")
                    * Decimal(f"{transaction["matecoin_price"]}")
                )
            if transaction["sold"] is not None:
                amount_matecoin -= Decimal(f"{transaction["sold"]}")
                profit += (
                    Decimal(f"{transaction["sold"]}")
                    * Decimal(f"{transaction["matecoin_price"]}")
                )

    profit_dict = {
        "earned_money": f"{profit}",
        "matecoin_account": f"{amount_matecoin}"
    }
    with open("profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2)
