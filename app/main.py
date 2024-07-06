import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades_lst = json.load(file)

    prof = {"earned_money": Decimal("0"), "matecoin_account": Decimal("0")}
    for trade in trades_lst:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = trade.get("matecoin_price")

        if bought is not None:
            prof["earned_money"] -= Decimal(bought) * Decimal(matecoin_price)
            prof["matecoin_account"] += Decimal(bought)
        if sold is not None:
            prof["earned_money"] += Decimal(sold) * Decimal(matecoin_price)
            prof["matecoin_account"] -= Decimal(sold)

    prof = {key: str(value) for key, value in prof.items()}

    with open("profit.json", "w") as file:
        json.dump(prof, file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
