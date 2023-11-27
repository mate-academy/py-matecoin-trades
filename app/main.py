import json
import decimal


def calculate_profit(file_name: str):
    with open(file_name,) as f:
        trades = json.load(f)

    money = decimal.Decimal("0.0")
    coin = decimal.Decimal("0.0")
    for trade in trades:
        if trade["bought"] is not None:
            money -= decimal.Decimal(trade["matecoin_price"]) * decimal.Decimal(trade["bought"])
            coin += decimal.Decimal(trade["bought"])
        if trade["sold"] is not None:
            money += decimal.Decimal(trade["matecoin_price"]) * decimal.Decimal(trade["sold"])
            coin -= decimal.Decimal(trade["sold"])
    data = {
        "earned_money": str(money),
        "matecoin_account": str(coin),
    }
    with open("profit.json", 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=2)
