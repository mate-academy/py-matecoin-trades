import json
import decimal


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as f:
        trades = json.load(f)

    profit = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            price = decimal.Decimal(trade["matecoin_price"])
            bought = decimal.Decimal(trade["bought"])
            profit -= price * bought
            matecoin_account += bought

        if trade["sold"] is not None:
            price = decimal.Decimal(trade["matecoin_price"])
            sold = decimal.Decimal(trade["sold"])
            profit += price * sold
            matecoin_account -= sold

    json_data = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_account),
    }
    with open("profit.json", "w") as f:
        json.dump(json_data, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
