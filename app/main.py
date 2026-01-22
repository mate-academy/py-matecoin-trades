import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r", encoding="utf-8") as f:
        trades = json.load(f)

    profit = decimal.Decimal("0")
    coin_acount = decimal.Decimal("0")

    for trade in trades:
        if not trade["bought"] is None:
            coin_acount += decimal.Decimal(trade["bought"])
            profit -= (decimal.Decimal(trade["bought"])
                       * decimal.Decimal(trade["matecoin_price"]))
        if not trade["sold"] is None:
            coin_acount -= decimal.Decimal(trade["sold"])
            profit += (decimal.Decimal(trade["sold"])
                       * decimal.Decimal(trade["matecoin_price"]))

    info = {"earned_money": str(profit), "matecoin_account": str(coin_acount)}

    with open("profit.json", "w") as f:
        json.dump(info, f, indent=2)
