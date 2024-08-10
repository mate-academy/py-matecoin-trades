import json
from decimal import Decimal


def calculate_profit(fla_name: str) -> None:
    bought = Decimal("0")
    sold = Decimal("0")
    mate_bought = Decimal("0")
    mate_sold = Decimal("0")
    with open(fla_name, "r") as source:
        data = json.load(source)
    for day in data:
        if day["bought"]:
            bought += Decimal(day.get("bought"))
            mate_bought += (
                Decimal(day.get("bought"))
                * Decimal(day.get("matecoin_price"))
            )
        if day["sold"]:
            sold += Decimal(day.get("sold"))
            mate_sold += (
                Decimal(day.get("sold"))
                * Decimal(day.get("matecoin_price"))
            )
    result_dict = {
        "earned_money": str(mate_sold - mate_bought),
        "matecoin_account": str(bought - sold)
    }
    with open("profit.json", "w") as dest:
        json.dump(result_dict, dest, indent=2)
