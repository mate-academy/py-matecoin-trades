import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit = Decimal("0")
    matecoin_account = Decimal("0")

    with open(file_name, "r", encoding="utf-8") as file:
        data: list[dict[str, str | None]] = json.load(file)

        for item in data:
            bought = Decimal(item.get("bought") or "0")
            sold = Decimal(item.get("sold") or "0")
            price = Decimal(item.get("matecoin_price") or "0")

            profit += (sold * price) - (bought * price)
            matecoin_account += bought - sold

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(
            {
                "earned_money": str(profit),
                "matecoin_account": str(matecoin_account)
            },
            file,
            indent=2
        )
