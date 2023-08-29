import json
from decimal import Decimal


def calculate_profit(trades_path: str) -> None:

    with open(trades_path, "r") as trades_deals:
        data_deals = json.load(trades_deals)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for deal in data_deals:
        bought = deal["bought"]
        sold = deal["sold"]
        matecoin_price = deal["matecoin_price"]

        if bought is None:
            earned_money += (Decimal(sold) * Decimal(matecoin_price))
            matecoin_account -= Decimal(sold)

        elif bought is not None and sold is not None:
            sub = Decimal(sold) - Decimal(bought)
            earned_money += (sub * Decimal(matecoin_price))
            matecoin_account -= sub

        else:
            earned_money -= (Decimal(bought) * Decimal(matecoin_price))
            matecoin_account += Decimal(bought)

    profite = {
        "earned_money": f"{earned_money}",
        "matecoin_account": f"{matecoin_account}"
    }
    with open("profit.json", "w") as json_file:
        json.dump(profite, json_file, indent=2)
