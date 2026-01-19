import json
from decimal import Decimal


def calculate_profit(traders_file: str) -> None:

    def get_decimal(value: str) -> Decimal:
        return Decimal(value) if value is not None else Decimal("0")

    profit = Decimal("0")
    matecoin_account = Decimal("0")

    with open(traders_file, "rb") as json_file:
        traders_stats = json.load(json_file)

    for stats in traders_stats:
        bought_coin = get_decimal(stats.get("bought"))
        sold_coin = get_decimal(stats.get("sold"))
        matecoin_price = get_decimal(stats.get("matecoin_price"))

        profit += (sold_coin - bought_coin) * matecoin_price
        matecoin_account += bought_coin - sold_coin

    profit_stats = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as stats_file:
        json.dump(profit_stats, stats_file, indent=2)
