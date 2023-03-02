import json
import decimal


def calculate_profit(trades: str) -> None:
    coin_wallet = decimal.Decimal("0")
    fiat_wallet = decimal.Decimal("0")
    result = dict()
    with open(trades, "r") as f:
        logs = json.load(f)

    for day in logs:
        if day.get("bought"):
            coin_wallet += decimal.Decimal(day["bought"])
            fiat_wallet -= decimal.Decimal(day["bought"]) * decimal.Decimal(
                day["matecoin_price"]
            )
        if day.get("sold"):
            coin_wallet -= decimal.Decimal(day["sold"])
            fiat_wallet += decimal.Decimal(day["sold"]) * decimal.Decimal(
                day["matecoin_price"]
            )

        result.update(
            {"earned_money": str(fiat_wallet),
             "matecoin_account": str(coin_wallet)}
        )
        with open("profit.json", "w") as f:
            json.dump(result, f, indent=2)
