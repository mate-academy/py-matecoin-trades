import json
import decimal


def calculate_profit(trades: list = None) -> None:
    if isinstance(trades, str):
        with open(trades, "r") as f:
            trades = json.load(f)
    elif trades is None:
        with open("trades.json", "r") as f:
            trades = json.load(f)

    total_earns = decimal.Decimal("0.0")
    total_buys = decimal.Decimal("0.0")
    account = decimal.Decimal("0.0")

    for trade in trades:
        mate = decimal.Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = decimal.Decimal(trade["bought"])
            total_buys += bought * mate
            account += bought

        if trade["sold"] is not None:
            sold = decimal.Decimal(trade["sold"])
            total_earns += sold * mate
            account -= sold

    final_dict = {
        "earned_money": str(total_earns - total_buys),
        "matecoin_account": str(account)
    }

    output_path = "profit.json"

    with open(output_path, "w") as f:
        json.dump(final_dict, f, indent=2)
