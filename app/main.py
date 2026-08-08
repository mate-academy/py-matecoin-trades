import json
from decimal import Decimal


def calculate_profit(filename: str = "app/trades.json") -> None:
    with open(filename, "r") as fname:
        trade = json.load(fname)
    account = {"earned_money": Decimal("0"), "matecoin_account": Decimal("0")}
    for deal in trade:
        if deal["bought"]:
            turnover = Decimal(deal["bought"]) * Decimal(
                deal["matecoin_price"]
            )
            account["earned_money"] -= turnover
            account["matecoin_account"] += Decimal(deal["bought"])
        if deal["sold"]:
            turnover = Decimal(deal["sold"]) * Decimal(deal["matecoin_price"])
            account["earned_money"] += turnover
            account["matecoin_account"] -= Decimal(deal["sold"])
    to_dump = {
        "earned_money": str(
            account["earned_money"].quantize(
                Decimal("1.0000000"), rounding="ROUND_HALF_UP"
            )
        ),
        "matecoin_account": str(
            account["matecoin_account"].quantize(
                Decimal("1.00000"), rounding="ROUND_HALF_UP"
            )
        )
    }
    with open("profit.json", "w") as fname:
        json.dump(to_dump, fname, indent=2)


calculate_profit()


if __name__ == "__main__":
    pass
